from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.conf import settings
import json
import logging
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod

from helper_api import (
    config, logger, TokenManager, OpenAIClient,
    EasyInputMessageParam, get_default_messages,
    ResponseProcessor, error_handler
)

logger = logging.getLogger(__name__)


class BaseDemo(ABC):
    """デモ機能の基底クラス（Django版）"""

    def __init__(self, demo_name: str):
        self.demo_name = demo_name
        self.config = config
        
        try:
            self.client = OpenAIClient()
        except Exception as e:
            logger.error(f"OpenAIクライアントの初期化に失敗しました: {e}")
            raise e

    def get_default_model(self) -> str:
        """デフォルトモデルを取得"""
        return self.config.get("models.default", "gpt-4o-mini")

    def is_reasoning_model(self, model: str = None) -> bool:
        """推論系モデルかどうかを判定"""
        if model is None:
            model = self.get_default_model()

        reasoning_models = self.config.get("models.categories.reasoning",
                                          ["o1", "o1-mini", "o3", "o3-mini", "o4", "o4-mini"])
        frontier_models = self.config.get("models.categories.frontier",
                                         ["gpt-5", "gpt-5-mini", "gpt-5-nano"])

        reasoning_indicators = ["o1", "o3", "o4", "gpt-5"]
        return any(indicator in model.lower() for indicator in reasoning_indicators) or \
            any(reasoning_model in model for reasoning_model in reasoning_models) or \
            any(frontier_model in model for frontier_model in frontier_models)

    @error_handler
    def call_api_unified(self, messages: List[EasyInputMessageParam], 
                        model: str = None, temperature: Optional[float] = None, **kwargs):
        """統一されたAPI呼び出し"""
        if model is None:
            model = self.get_default_model()

        api_params = {
            "input": messages,
            "model": model
        }

        if not self.is_reasoning_model(model) and temperature is not None:
            api_params["temperature"] = temperature

        api_params.update(kwargs)
        return self.client.create_response(**api_params)

    @abstractmethod
    def process_query(self, user_input: str, **kwargs):
        """各デモの処理ロジック（サブクラスで実装）"""
        pass


class TextResponseDemo(BaseDemo):
    """基本的なテキスト応答のデモ（Django版）"""

    def __init__(self):
        super().__init__("TextResponseDemo")

    def process_query(self, user_input: str, model: str = None, temperature: Optional[float] = None):
        """クエリの処理"""
        if model is None:
            model = self.get_default_model()

        # デフォルトメッセージを取得
        messages = get_default_messages()
        messages.append(
            EasyInputMessageParam(role="user", content=user_input)
        )

        # API呼び出し
        response = self.call_api_unified(messages, model=model, temperature=temperature)
        
        # レスポンスを処理
        result = ResponseProcessor.format_response(response)
        
        return {
            'success': True,
            'response': result,
            'texts': ResponseProcessor.extract_text(response),
            'model': model,
            'input_tokens': result.get('usage', {}).get('prompt_tokens', 0),
            'output_tokens': result.get('usage', {}).get('completion_tokens', 0),
            'total_tokens': result.get('usage', {}).get('total_tokens', 0)
        }


@login_required
def index(request):
    """テストレスポンスデモのメインページ"""
    context = {
        'demo_name': 'TextResponseDemo',
        'available_models': config.get("models.available", ["gpt-4o-mini", "gpt-4o"]),
        'default_model': config.get("models.default", "gpt-4o-mini"),
        'example_query': config.get("samples.prompts.responses_query", 
                                   "OpenAIのAPIで、responses.createを説明しなさい。")
    }
    return render(request, 'test_response_demo/index.html', context)


@login_required
@require_http_methods(["POST"])
@csrf_exempt
def process_query(request):
    """クエリ処理のAPI"""
    try:
        data = json.loads(request.body)
        user_input = data.get('user_input', '').strip()
        model = data.get('model', config.get("models.default", "gpt-4o-mini"))
        temperature = data.get('temperature')
        
        if not user_input:
            return JsonResponse({
                'success': False,
                'error': '入力テキストが空です'
            })

        # TextResponseDemoを実行
        demo = TextResponseDemo()
        result = demo.process_query(user_input, model=model, temperature=temperature)
        
        return JsonResponse(result)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON format'
        })
    except Exception as e:
        logger.error(f"クエリ処理エラー: {e}")
        return JsonResponse({
            'success': False,
            'error': str(e)
        })


@login_required
def get_model_info(request, model_name):
    """モデル情報を取得"""
    try:
        limits = TokenManager.get_model_limits(model_name)
        pricing = config.get("model_pricing", {}).get(model_name, {})
        
        demo = TextResponseDemo()
        is_reasoning = demo.is_reasoning_model(model_name)
        
        return JsonResponse({
            'success': True,
            'model_name': model_name,
            'limits': limits,
            'pricing': pricing,
            'is_reasoning_model': is_reasoning,
            'supports_temperature': not is_reasoning
        })
    except Exception as e:
        logger.error(f"モデル情報取得エラー: {e}")
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
