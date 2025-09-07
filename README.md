## Django + OpenAI API From Scratch
## スクラッチで (Django + OpenAI API)

## 🔗 関連プロジェクト## 🔗 関連プロジェクト

| プロジェクト                                                             | 説明                                         | ステータス |
| ------------------------------------------------------------------------ | -------------------------------------------- | ---------- |
| [openai_api_jp](https://github.com/nakashima2toshio/openai_api_jp)       | OpenAI API完全ガイド（本プロジェクト）       | ✅ 公開中  |
| [anthropic_api_jp](https://github.com/nakashima2toshio/anthropic_api_jp) | Anthropic Claude API活用                     | ✅ 公開中  |
| [openai_rag_jp](https://github.com/nakashima2toshio/openai_rag_jp)       | RAG実装パターン集（cloud版、Local-Qdrant版） | ✅ 公開中  |
| [openai_mcp_jp](https://github.com/nakashima2toshio/openai_mcp_jp)       | MCP(Model Context Protocol)実装              | 🚧 整備中  |
| [openai_django_jp](https://github.com/nakashima2toshio/openai_django_jp) | OpenAI API + Django実装                      | ✅ 公開中  |
| [openai_agent_jp](https://github.com/nakashima2toshio/openai_agent_jp)   | AIエージェント構築                           | 📝 作成中  |

## DjangoでOpenAI APIマスター - 完全ガイド

<div>

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.5-green)](https://www.djangoproject.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

### Quick Start：

[README_Start.md](./README_Start.md)

## 📚 目次

1. [プロジェクト概要](#-プロジェクト概要)
2. [システムアーキテクチャ](#-システムアーキテクチャ)
3. [クイックスタート](#-クイックスタート)
4. [詳細セットアップ](#-詳細セットアップ)
5. [Django基本機能](#-django基本機能)
6. [OpenAI API統合](#-openai-api統合)
7. [test_response_demoアプリ詳細](#-test_response_demoアプリ詳細)
8. [新規OpenAI APIアプリ作成ガイド](#-新規openai-apiアプリ作成ガイド)
9. [データベース設計](#-データベース設計)
10. [開発・運用](#-開発運用)
11. [トラブルシューティング](#-トラブルシューティング)

---

## 🎯 プロジェクト概要

このプロジェクトは、**DjangoフレームワークとOpenAI APIの統合**を学習・実装するための包括的なテンプレートです。実践的なサンプルアプリケーションを通じて、モダンなWeb開発とAI統合の手法を習得できます。

### 主要機能

- 🔐 **完全な認証システム** - django-allauthによる多機能認証
- 📝 **タスク管理システム** - CRUDアプリケーションのサンプル実装
- 🤖 **OpenAI API統合** - helper_api.pyによる効率的なAPI管理
- 🎨 **レスポンシブUI** - Bootstrap5による洗練されたインターフェース
- 🧪 **包括的なテスト** - ユニットテストとインテグレーションテスト
- 🌐 **国際化対応** - 日本語環境に最適化

---

## 🏗️ システムアーキテクチャ

### プロジェクト構造

```
openai_django_jp/
│
├── 📁 django_web_allauth/      # メインDjangoプロジェクト設定
│   ├── settings.py              # プロジェクト設定
│   ├── urls.py                  # ルートURLコンフィグ
│   ├── wsgi.py                  # WSGI設定
│   └── asgi.py                  # ASGI設定
│
├── 📁 accounts/                 # カスタムユーザー認証アプリ
│   ├── models.py                # CustomUserモデル定義
│   ├── views.py                 # 認証関連ビュー
│   ├── forms.py                 # カスタムフォーム
│   ├── admin.py                 # 管理画面設定
│   ├── tests/                   # テストケース
│   └── templates/               # 認証用テンプレート
│
├── 📁 todo_task/                # タスク管理アプリ
│   ├── models.py                # Taskモデル定義
│   ├── views.py                 # CRUD操作ビュー
│   ├── forms.py                 # タスクフォーム
│   ├── urls.py                  # URLパターン
│   ├── tests/                   # ユニットテスト
│   └── templates/               # タスク管理UI
│
├── 📁 test_response_demo/       # OpenAI API統合デモ
│   ├── views.py                 # API呼び出しロジック
│   ├── urls.py                  # APIエンドポイント
│   ├── apps.py                  # アプリ設定
│   └── templates/               # デモUI
│
├── 📁 templates/                # 共通テンプレート
│   ├── base.html                # ベーステンプレート
│   └── home.html                # ホームページ
│
├── 📁 static/                   # 静的ファイル
│   ├── css/                     # スタイルシート
│   ├── js/                      # JavaScript
│   └── images/                  # 画像ファイル
│
├── 📁 docker_compose/           # Docker設定
│   ├── docker-compose.yml       # PostgreSQL構成
│   └── docker-compose-mysql.yml # MySQL構成
│
├── 📄 helper_api.py             # OpenAI APIヘルパー
├── 📄 helper_st.py              # Streamlitヘルパー
├── 📄 config.yml                # API設定ファイル
├── 📄 requirements.txt          # 依存パッケージ
├── 📄 manage.py                 # Django管理コマンド
└── 📄 .env.example              # 環境変数テンプレート
```

### 技術スタック


| カテゴリ     | 技術           | バージョン | 用途              |
| ------------ | -------------- | ---------- | ----------------- |
| **Backend**  | Python         | 3.9+       | メイン言語        |
|              | Django         | 5.2.5      | Webフレームワーク |
|              | django-allauth | 65.9.0     | 認証システム      |
| **AI/ML**    | OpenAI API     | 1.55.0+    | AI機能            |
|              | tiktoken       | 0.8.0+     | トークン計算      |
| **Frontend** | Bootstrap      | 5.x        | UIフレームワーク  |
|              | JavaScript     | ES6+       | 動的UI            |
| **Database** | SQLite3        | -          | 開発用DB          |
|              | PostgreSQL     | 15+        | 本番用DB          |
|              | MySQL          | 8.0+       | 代替DB            |
| **Tools**    | Docker         | 20.10+     | コンテナ化        |
|              | Git            | 2.x        | バージョン管理    |

---

## 🚀 クイックスタート

### 前提条件

- Python 3.9以上
- pip（Pythonパッケージマネージャー）
- Git
- OpenAI APIキー（[取得方法](https://platform.openai.com/api-keys)）

### 30秒セットアップ

```bash
# 1. リポジトリをクローン
git clone <repository-url>
cd openai_django_jp

# 2. 仮想環境を作成・有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 依存パッケージをインストール
pip install -r requirements.txt

# 4. 環境変数を設定
echo "OPENAI_API_KEY=your-api-key-here" > .env

# 5. データベースを初期化
python manage.py migrate
python manage.py createsuperuser

# 6. サーバーを起動
python manage.py runserver
```

ブラウザで http://localhost:8000 にアクセス！

---

## 🔧 詳細セットアップ

### 環境変数設定

`.env` ファイルを作成し、以下の設定を記述：

```bash
# OpenAI API設定（必須）
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

# Django設定
SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxxxx
DEBUG=True  # 本番環境ではFalse
ALLOWED_HOSTS=localhost,127.0.0.1

# データベース設定（PostgreSQL使用時）
DATABASE_URL=postgres://user:password@localhost:5432/dbname

# メール設定（本番環境用）
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# ログレベル
LOG_LEVEL=INFO
```

### OpenAI API設定（config.yml）

```yaml
# config.yml - OpenAI API詳細設定
models:
  default: "gpt-4o-mini"      # デフォルトモデル
  available:
    - "gpt-4o"                 # 高性能モデル
    - "gpt-4o-mini"            # コスト効率モデル
    - "gpt-4.1"                # 最新版
    - "gpt-4.1-mini"           # 軽量版
    - "o1"                     # 推論特化
    - "o3"                     # 高度推論

api:
  timeout: 30                  # タイムアウト（秒）
  max_retries: 3               # リトライ回数
  message_limit: 50            # メッセージ履歴上限

cache:
  enabled: true                # キャッシュ有効化
  ttl: 3600                    # キャッシュ有効期限（秒）
  max_size: 100                # 最大キャッシュ数

model_pricing:                 # モデル別料金（USD/1000トークン）
  gpt-4o-mini:
    input: 0.00015
    output: 0.0006
  gpt-4o:
    input: 0.005
    output: 0.015

logging:
  level: "INFO"                # ログレベル
  file: "logs/openai_api.log"  # ログファイル
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### データベースセットアップ

#### SQLite3（デフォルト・開発用）

```bash
# マイグレーション実行
python manage.py makemigrations
python manage.py migrate

# スーパーユーザー作成
python manage.py createsuperuser
```

#### PostgreSQL（Docker使用）

```bash
# PostgreSQLコンテナ起動
cd docker_compose
docker-compose up -d

# settings.pyで設定切り替え
# DATABASES設定のコメントを外す
```

#### MySQL（Docker使用）

```bash
# MySQLコンテナ起動
cd docker_compose
docker-compose -f docker-compose-mysql.yml up -d
```

---

## 🎮 Django基本機能

### django-allauthによる認証機能


| カテゴリ               | 機能               | 説明                               |
| ---------------------- | ------------------ | ---------------------------------- |
| **ユーザー登録と認証** | Sign Up            | 新規ユーザー登録（メール確認付き） |
|                        | Login              | ユーザー名/メールでログイン        |
|                        | Logout             | セッション終了                     |
| **パスワード管理**     | Password Reset     | メール経由でパスワードリセット     |
|                        | Password Change    | ログイン後のパスワード変更         |
|                        | Password Set       | ソーシャルログイン後の設定         |
| **ソーシャル認証**     | Social Login       | Google/Facebook/Twitter連携        |
|                        | Account Linking    | 複数認証方法の紐付け               |
| **アカウント管理**     | Email Management   | メールアドレスの追加/削除/確認     |
|                        | User Profile       | プロファイル編集                   |
| **セキュリティ**       | Session Management | セッション管理・無効化             |
|                        | Rate Limiting      | ログイン試行制限                   |
|                        | MFA                | 多要素認証（TOTP対応）             |

### カスタムユーザーモデル

```python
# accounts/models.py
class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""
    objects = CustomUserManager()
  
    # カスタムフィールド（必要に応じて追加）
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
  
    def __str__(self):
        return self.email
```

### タスク管理システム（todo_task）

```python
# todo_task/models.py
class Task(models.Model):
    """タスクモデル"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta:
        ordering = ['-priority', 'due_date']
  
    def __str__(self):
        return self.title
```

---

## 🤖 OpenAI API統合

### helper_api.pyの主要機能

#### 1. 設定管理（ConfigManager）

```python
from helper_api import config

# 設定値の取得
model = config.get("models.default")  # "gpt-4o-mini"
timeout = config.get("api.timeout")   # 30

# 動的設定変更
config.set("models.default", "gpt-4o")
```

#### 2. APIクライアント（OpenAIClient）

```python
from helper_api import OpenAIClient, get_default_messages

# クライアント初期化
client = OpenAIClient()

# 基本的な使用例
messages = get_default_messages()
messages.append({
    "role": "user",
    "content": "Pythonでクイックソートを実装してください"
})

# API呼び出し
response = client.create_response(
    input=messages,
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1000
)
```

#### 3. レスポンス処理（ResponseProcessor）

```python
from helper_api import ResponseProcessor

# レスポンスからテキスト抽出
texts = ResponseProcessor.extract_text(response)

# レスポンスの整形
formatted = ResponseProcessor.format_response(response)
print(f"使用トークン: {formatted['usage']['total_tokens']}")

# レスポンス保存
filepath = ResponseProcessor.save_response(response, "response_001.json")
```

#### 4. トークン管理（TokenManager）

```python
from helper_api import TokenManager

# トークン数計算
text = "これは長いテキストです..."
tokens = TokenManager.count_tokens(text, model="gpt-4o-mini")

# テキスト切り詰め
truncated = TokenManager.truncate_text(text, max_tokens=100)

# コスト推定
cost = TokenManager.estimate_cost(
    input_tokens=1000,
    output_tokens=500,
    model="gpt-4o-mini"
)
print(f"推定コスト: ${cost:.4f}")
```

#### 5. メッセージ管理（MessageManager）

```python
from helper_api import MessageManager

# メッセージ履歴管理
manager = MessageManager()

# メッセージ追加
manager.add_message("user", "質問です")
manager.add_message("assistant", "回答です")

# 履歴取得
messages = manager.get_messages()

# エクスポート/インポート
data = manager.export_messages()
manager.import_messages(data)
```

### Django Viewでの実装例

```python
# views.py
from django.http import JsonResponse
from helper_api import OpenAIClient, ResponseProcessor, error_handler

class AIAssistantView(View):
    def __init__(self):
        self.client = OpenAIClient()
  
    @error_handler
    def post(self, request):
        user_input = request.POST.get('message')
  
        # メッセージ構築
        messages = [
            {"role": "system", "content": "あなたは親切なアシスタントです"},
            {"role": "user", "content": user_input}
        ]
  
        # API呼び出し
        response = self.client.create_response(
            input=messages,
            model="gpt-4o-mini",
            temperature=0.7
        )
  
        # レスポンス処理
        texts = ResponseProcessor.extract_text(response)
  
        return JsonResponse({
            'success': True,
            'response': texts[0] if texts else '',
            'usage': response.usage.dict() if response.usage else {}
        })
```

---

## 📱 test_response_demoアプリ詳細

### アプリ構造

```
test_response_demo/
├── __init__.py
├── apps.py                 # アプリ設定
├── models.py               # モデル定義（現在は空）
├── views.py                # ビューロジック
│   ├── BaseDemo           # 基底クラス
│   ├── TextResponseDemo   # テキスト応答デモ
│   ├── index              # メインページ
│   ├── process_query      # クエリ処理API
│   └── get_model_info     # モデル情報API
├── urls.py                 # URLパターン
│   ├── ''                 # メインページ
│   ├── 'process/'         # 処理エンドポイント
│   └── 'model/<str>/info/' # モデル情報
└── templates/
    └── test_response_demo/
        └── index.html      # UIテンプレート
```

### 主要コンポーネント

#### 1. BaseDemo基底クラス

```python
class BaseDemo(ABC):
    """デモ機能の基底クラス"""
  
    def __init__(self, demo_name: str):
        self.demo_name = demo_name
        self.config = config
        self.client = OpenAIClient()
  
    def get_default_model(self) -> str:
        """デフォルトモデル取得"""
        return self.config.get("models.default", "gpt-4o-mini")
  
    def is_reasoning_model(self, model: str = None) -> bool:
        """推論系モデル判定"""
        # o1, o3, o4, gpt-5系は推論モデル
  
    @error_handler
    def call_api_unified(self, messages, model=None, temperature=None):
        """統一API呼び出し"""
        # 推論モデルはtemperature非対応
  
    @abstractmethod
    def process_query(self, user_input: str, **kwargs):
        """処理ロジック（サブクラスで実装）"""
        pass
```

#### 2. TextResponseDemo実装

```python
class TextResponseDemo(BaseDemo):
    """テキスト応答デモ"""
  
    def process_query(self, user_input: str, model=None, temperature=None):
        # デフォルトメッセージ構築
        messages = get_default_messages()
        messages.append(
            EasyInputMessageParam(role="user", content=user_input)
        )
  
        # API呼び出し
        response = self.call_api_unified(
            messages, 
            model=model, 
            temperature=temperature
        )
  
        # 結果整形
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
```

#### 3. フロントエンド機能

- **リアルタイムトークン推定**: 入力時に自動計算
- **モデル情報表示**: 料金、制限、特性を動的表示
- **温度パラメータ制御**: スライダーで創造性調整
- **レスポンス詳細表示**: トークン使用量、レスポンスID
- **エラーハンドリング**: ユーザーフレンドリーなエラー表示

### API エンドポイント


| エンドポイント                                 | メソッド | 説明           | パラメータ                     |
| ---------------------------------------------- | -------- | -------------- | ------------------------------ |
| `/test_response_demo/`                         | GET      | デモページ表示 | -                              |
| `/test_response_demo/process/`                 | POST     | クエリ処理     | user_input, model, temperature |
| `/test_response_demo/model/<model_name>/info/` | GET      | モデル情報取得 | model_name                     |

---

## 🛠️ 新規OpenAI APIアプリ作成ガイド

### ステップ1: Djangoアプリ作成

```bash
# 新規アプリ作成
python manage.py startapp ai_chat

# settings.pyに追加
INSTALLED_APPS = [
    # ...
    'ai_chat',
]
```

### ステップ2: モデル定義

```python
# ai_chat/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatSession(models.Model):
    """チャットセッション"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
class ChatMessage(models.Model):
    """チャットメッセージ"""
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)  # user, assistant, system
    content = models.TextField()
    tokens_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

### ステップ3: ビュー実装

```python
# ai_chat/views.py
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from helper_api import OpenAIClient, ResponseProcessor, MessageManager

class ChatView(LoginRequiredMixin, View):
    """AIチャットビュー"""
  
    def __init__(self):
        super().__init__()
        self.client = OpenAIClient()
  
    def get(self, request):
        """チャット画面表示"""
        context = {
            'available_models': config.get("models.available"),
            'default_model': config.get("models.default"),
        }
        return render(request, 'ai_chat/chat.html', context)
  
    def post(self, request):
        """メッセージ処理"""
        data = json.loads(request.body)
        session_id = data.get('session_id')
        message = data.get('message')
        model = data.get('model', 'gpt-4o-mini')
  
        # セッション取得または作成
        session = self._get_or_create_session(request.user, session_id)
  
        # メッセージ履歴構築
        messages = self._build_message_history(session)
        messages.append({"role": "user", "content": message})
  
        # API呼び出し
        response = self.client.create_response(
            input=messages,
            model=model,
            temperature=0.7,
            stream=False  # ストリーミングも可能
        )
  
        # レスポンス処理と保存
        assistant_message = self._process_and_save_response(
            session, message, response
        )
  
        return JsonResponse({
            'success': True,
            'message': assistant_message,
            'session_id': session.id
        })
  
    def _get_or_create_session(self, user, session_id=None):
        """セッション取得または作成"""
        if session_id:
            return ChatSession.objects.get(id=session_id, user=user)
        return ChatSession.objects.create(
            user=user,
            title=f"チャット {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
  
    def _build_message_history(self, session):
        """メッセージ履歴構築"""
        messages = []
        for msg in session.chatmessage_set.order_by('created_at')[-10:]:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        return messages
  
    def _process_and_save_response(self, session, user_message, response):
        """レスポンス処理と保存"""
        # ユーザーメッセージ保存
        ChatMessage.objects.create(
            session=session,
            role="user",
            content=user_message,
            tokens_used=response.usage.prompt_tokens if response.usage else 0
        )
  
        # アシスタントメッセージ抽出と保存
        texts = ResponseProcessor.extract_text(response)
        assistant_message = texts[0] if texts else "申し訳ございません。応答を生成できませんでした。"
  
        ChatMessage.objects.create(
            session=session,
            role="assistant",
            content=assistant_message,
            tokens_used=response.usage.completion_tokens if response.usage else 0
        )
  
        return assistant_message
```

### ステップ4: URLパターン設定

```python
# ai_chat/urls.py
from django.urls import path
from . import views

app_name = 'ai_chat'

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
    path('sessions/', views.SessionListView.as_view(), name='sessions'),
    path('session/<int:pk>/', views.SessionDetailView.as_view(), name='session_detail'),
]

# メインurls.pyに追加
urlpatterns = [
    # ...
    path('ai-chat/', include('ai_chat.urls')),
]
```

### ステップ5: テンプレート作成

```html
<!-- ai_chat/templates/ai_chat/chat.html -->
{% extends 'base.html' %}

{% block content %}
<div class="container mt-4">
    <div class="row">
        <div class="col-md-3">
            <!-- セッション一覧 -->
            <div class="card">
                <div class="card-header">
                    <h6>チャット履歴</h6>
                </div>
                <div class="card-body">
                    <button class="btn btn-primary btn-sm w-100 mb-2" id="newChatBtn">
                        新規チャット
                    </button>
                    <div id="sessionList"></div>
                </div>
            </div>
        </div>
  
        <div class="col-md-9">
            <!-- チャットエリア -->
            <div class="card">
                <div class="card-header">
                    <h5>AIチャット</h5>
                </div>
                <div class="card-body">
                    <div id="chatMessages" style="height: 400px; overflow-y: auto;">
                        <!-- メッセージ表示エリア -->
                    </div>
                </div>
                <div class="card-footer">
                    <div class="input-group">
                        <input type="text" class="form-control" id="messageInput" 
                               placeholder="メッセージを入力...">
                        <button class="btn btn-primary" id="sendBtn">送信</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// チャット機能のJavaScript実装
document.addEventListener('DOMContentLoaded', function() {
    let currentSessionId = null;
  
    // メッセージ送信
    document.getElementById('sendBtn').addEventListener('click', sendMessage);
    document.getElementById('messageInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendMessage();
    });
  
    function sendMessage() {
        const input = document.getElementById('messageInput');
        const message = input.value.trim();
        if (!message) return;
  
        // UIに表示
        appendMessage('user', message);
        input.value = '';
  
        // API呼び出し
        fetch('/ai-chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({
                session_id: currentSessionId,
                message: message,
                model: 'gpt-4o-mini'
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                currentSessionId = data.session_id;
                appendMessage('assistant', data.message);
            }
        });
    }
  
    function appendMessage(role, content) {
        const messagesDiv = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        messageDiv.innerHTML = `
            <div class="mb-3">
                <strong>${role === 'user' ? 'You' : 'AI'}:</strong>
                <div>${content}</div>
            </div>
        `;
        messagesDiv.appendChild(messageDiv);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
});
</script>
{% endblock %}
```

### ステップ6: 高度な機能の追加

#### ストリーミング対応

```python
# views.py - ストリーミングレスポンス
from django.http import StreamingHttpResponse
import json

def stream_chat(request):
    """ストリーミングチャット"""
    def generate():
        # ストリーミングAPI呼び出し
        stream = client.create_response(
            input=messages,
            model="gpt-4o-mini",
            stream=True
        )
  
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield f"data: {json.dumps({'content': chunk.choices[0].delta.content})}\n\n"
  
    return StreamingHttpResponse(
        generate(),
        content_type='text/event-stream'
    )
```

#### 関数呼び出し（Function Calling）

```python
# 関数定義
functions = [
    {
        "name": "get_weather",
        "description": "指定された場所の天気を取得",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "都市名"
                }
            },
            "required": ["location"]
        }
    }
]

# API呼び出し
response = client.create_response(
    input=messages,
    model="gpt-4o",
    functions=functions,
    function_call="auto"
)
```

#### 画像入力対応

```python
# 画像付きメッセージ
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "この画像を説明してください"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }
]
```

---

## 🗂️ データベース設計

### ER図（更新版）

```mermaid
erDiagram
    CustomUser ||--o{ Task : "has"
    CustomUser ||--o{ SocialAccount : "has"
    CustomUser ||--o{ EmailAddress : "has"
    CustomUser ||--o{ ChatSession : "has"
    ChatSession ||--o{ ChatMessage : "contains"
  
    CustomUser {
        int id PK
        string username UK
        string email UK
        string password
        boolean is_active
        boolean is_staff
        boolean is_superuser
        datetime date_joined
        datetime last_login
        string first_name
        string last_name
    }
  
    Task {
        int id PK
        int user_id FK
        string title
        text description
        date due_date
        boolean completed
        int priority
        datetime created_at
        datetime updated_at
    }
  
    SocialAccount {
        int id PK
        int user_id FK
        string provider
        string uid
        datetime date_joined
        text extra_data
    }
  
    EmailAddress {
        int id PK
        int user_id FK
        string email UK
        boolean verified
        boolean primary
    }
  
    ChatSession {
        int id PK
        int user_id FK
        string title
        datetime created_at
        datetime updated_at
    }
  
    ChatMessage {
        int id PK
        int session_id FK
        string role
        text content
        int tokens_used
        datetime created_at
    }
```

### インデックス設計

```python
# models.py - インデックス最適化
class Task(models.Model):
    # ...
    class Meta:
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['due_date', 'completed']),
        ]

class ChatMessage(models.Model):
    # ...
    class Meta:
        indexes = [
            models.Index(fields=['session', 'created_at']),
        ]
```

---

## 🔬 開発・運用

### テスト戦略

#### ユニットテスト

```python
# tests/test_openai_integration.py
from django.test import TestCase
from unittest.mock import patch, MagicMock
from helper_api import OpenAIClient

class OpenAIIntegrationTest(TestCase):
    """OpenAI統合テスト"""
  
    @patch('helper_api.OpenAI')
    def test_api_call_success(self, mock_openai):
        """API呼び出し成功テスト"""
        # モックレスポンス設定
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="テスト応答"))
        ]
        mock_openai.return_value.chat.completions.create.return_value = mock_response
  
        # テスト実行
        client = OpenAIClient()
        response = client.create_response(
            input=[{"role": "user", "content": "テスト"}],
            model="gpt-4o-mini"
        )
  
        # アサーション
        self.assertIsNotNone(response)
  
    def test_token_counting(self):
        """トークン計算テスト"""
        from helper_api import TokenManager
  
        text = "これはテストテキストです。"
        tokens = TokenManager.count_tokens(text, "gpt-4o-mini")
  
        self.assertGreater(tokens, 0)
        self.assertLess(tokens, 100)
```

#### 統合テスト

```python
# tests/test_views.py
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatViewTest(TestCase):
    """チャットビューテスト"""
  
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
  
    def test_chat_requires_login(self):
        """ログイン必須テスト"""
        response = self.client.get('/ai-chat/')
        self.assertEqual(response.status_code, 302)  # リダイレクト
  
    def test_chat_post_message(self):
        """メッセージ投稿テスト"""
        self.client.login(username='testuser', password='testpass123')
  
        response = self.client.post('/ai-chat/', {
            'message': 'テストメッセージ',
            'model': 'gpt-4o-mini'
        }, content_type='application/json')
  
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
```

### パフォーマンス最適化

#### キャッシング戦略

```python
# views.py - キャッシュ実装
from django.core.cache import cache
from helper_api import cache_result

class OptimizedChatView(View):
  
    @cache_result(ttl=3600)  # 1時間キャッシュ
    def get_similar_response(self, query):
        """類似応答をキャッシュ"""
        # キャッシュキー生成
        cache_key = f"chat_response_{hashlib.md5(query.encode()).hexdigest()}"
  
        # キャッシュチェック
        cached = cache.get(cache_key)
        if cached:
            return cached
  
        # API呼び出し
        response = self.client.create_response(...)
  
        # キャッシュ保存
        cache.set(cache_key, response, 3600)
        return response
```

#### データベース最適化

```python
# views.py - クエリ最適化
from django.db.models import Prefetch

def get_user_sessions(user):
    """ユーザーセッション取得（最適化）"""
    return ChatSession.objects.filter(user=user)\
        .select_related('user')\
        .prefetch_related(
            Prefetch('chatmessage_set',
                    queryset=ChatMessage.objects.order_by('-created_at')[:10])
        )\
        .order_by('-updated_at')[:10]
```

### セキュリティ対策

```python
# settings.py - セキュリティ設定
import os
from dotenv import load_dotenv

load_dotenv()

# 本番環境設定
if not DEBUG:
    # HTTPS強制
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
  
    # セキュリティヘッダー
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
  
    # HSTS
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# APIキー保護
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY must be set")

# レート制限
RATELIMIT_ENABLE = True
RATELIMIT_RATE = '100/h'  # 1時間あたり100リクエスト
```

### モニタリング

```python
# monitoring.py - 使用状況モニタリング
import logging
from datetime import datetime, timedelta
from django.db.models import Sum

logger = logging.getLogger('openai_monitor')

class UsageMonitor:
    """API使用状況モニター"""
  
    @staticmethod
    def log_api_usage(user, model, tokens_used, cost):
        """API使用ログ"""
        logger.info(f"API Usage: user={user.id}, model={model}, "
                   f"tokens={tokens_used}, cost=${cost:.4f}")
  
        # データベースに記録
        APIUsage.objects.create(
            user=user,
            model=model,
            tokens_used=tokens_used,
            cost=cost
        )
  
    @staticmethod
    def get_daily_usage(user, date=None):
        """日次使用量取得"""
        if date is None:
            date = datetime.now().date()
  
        return APIUsage.objects.filter(
            user=user,
            created_at__date=date
        ).aggregate(
            total_tokens=Sum('tokens_used'),
            total_cost=Sum('cost')
        )
  
    @staticmethod
    def check_rate_limit(user):
        """レート制限チェック"""
        one_hour_ago = datetime.now() - timedelta(hours=1)
        recent_count = APIUsage.objects.filter(
            user=user,
            created_at__gte=one_hour_ago
        ).count()
  
        if recent_count >= 100:  # 1時間100リクエスト制限
            raise RateLimitExceeded("API rate limit exceeded")
  
        return recent_count
```

---

## 🚀 デプロイメント

### Docker化

```dockerfile
# Dockerfile
FROM python:3.9-slim

# 作業ディレクトリ設定
WORKDIR /app

# 依存関係インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコピー
COPY . .

# 静的ファイル収集
RUN python manage.py collectstatic --noinput

# ポート公開
EXPOSE 8000

# 起動コマンド
CMD ["gunicorn", "django_web_allauth.wsgi:application", 
     "--bind", "0.0.0.0:8000", "--workers", "3"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    command: gunicorn django_web_allauth.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/static
      - media_volume:/app/media
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: django_db
      POSTGRES_USER: django_user
      POSTGRES_PASSWORD: ${DB_PASSWORD}

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/static
      - media_volume:/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### CI/CD（GitHub Actions）

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
  
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
  
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
  
      - name: Run tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python manage.py test
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd /var/www/openai_django_jp
            git pull origin main
            docker-compose down
            docker-compose up -d --build
            docker-compose exec web python manage.py migrate
```

---

## 🔧 トラブルシューティング

### よくある問題と解決方法

#### 1. OpenAI APIエラー

```python
# エラー処理の実装
from openai import OpenAIError, RateLimitError, APITimeoutError

try:
    response = client.create_response(...)
except RateLimitError as e:
    # レート制限エラー
    logger.error(f"Rate limit exceeded: {e}")
    return JsonResponse({
        'error': 'API利用制限に達しました。しばらくお待ちください。'
    }, status=429)
except APITimeoutError as e:
    # タイムアウトエラー
    logger.error(f"API timeout: {e}")
    return JsonResponse({
        'error': 'リクエストがタイムアウトしました。'
    }, status=504)
except OpenAIError as e:
    # その他のOpenAIエラー
    logger.error(f"OpenAI API error: {e}")
    return JsonResponse({
        'error': 'APIエラーが発生しました。'
    }, status=500)
```

#### 2. メモリ不足対策

```python
# ストリーミング処理でメモリ効率化
def process_large_text(text):
    """大きなテキストの処理"""
    chunk_size = 1000  # チャンクサイズ
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
  
    results = []
    for chunk in chunks:
        response = client.create_response(
            input=[{"role": "user", "content": chunk}],
            model="gpt-4o-mini"
        )
        results.append(response)
  
    return results
```

#### 3. データベース接続エラー

```bash
# PostgreSQL接続確認
python manage.py dbshell

# マイグレーションリセット
python manage.py migrate --fake-zero
python manage.py migrate

# データベース再作成
dropdb django_db
createdb django_db
python manage.py migrate
```

#### 4. 静的ファイル配信問題

```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 開発環境での静的ファイル配信
if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, 
                         document_root=settings.STATIC_ROOT)
```

### デバッグツール

```python
# settings.py - デバッグツール設定
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
  
    # Django Debug Toolbar設定
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }
```

---

## 📚 追加リソース

### 公式ドキュメント

- [Django公式ドキュメント](https://docs.djangoproject.com/)
- [OpenAI API リファレンス](https://platform.openai.com/docs/)
- [django-allauth ドキュメント](https://django-allauth.readthedocs.io/)
- [Bootstrap 5 ドキュメント](https://getbootstrap.com/docs/5.0/)

### 学習リソース

- [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)
- [OpenAI Cookbook](https://cookbook.openai.com/)

### コミュニティ

- [Django Forum](https://forum.djangoproject.com/)
- [r/django](https://www.reddit.com/r/django/)
- [OpenAI Community](https://community.openai.com/)

---

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🤝 コントリビューション

プルリクエストは歓迎します！大きな変更の場合は、まずissueを開いて変更内容を議論してください。

1. フォーク (`Fork`) する
2. フィーチャーブランチを作成する (`git checkout -b feature/AmazingFeature`)
3. 変更をコミットする (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュする (`git push origin feature/AmazingFeature`)
5. プルリクエストを開く

### コーディング規約

- PEP 8準拠
- 型ヒント使用推奨
- ドキュメント文字列必須
- テストカバレッジ80%以上

---

## 📮 お問い合わせ

- GitHub Issues: [プロジェクトのIssues](https://github.com/yourusername/openai_django_jp/issues)
- Email: your.email@example.com

---

<div align="center">

**Happy Coding! 🚀**

*最終更新: 2025年9月*

</div>
