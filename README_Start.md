# Django + OpenAI API 統合ガイド

## 📖 はじめに

このプロジェクトは、DjangoフレームワークとOpenAI APIを統合した包括的なWebアプリケーション開発環境です。ユーザー認証、タスク管理システム、そしてOpenAI APIとの統合機能を備えています。

## 🚀 クイックスタート

### 必要な環境

- Python 3.9以上
- pip（Pythonパッケージマネージャー）
- Git
- PostgreSQL または MySQL（オプション、デフォルトはSQLite3）

## 📦 環境構築

### 1. リポジトリのクローン

```bash
git clone <repository-url>
cd openai_django_jp
```

### 2. 仮想環境の作成と有効化

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. 環境変数の設定

プロジェクトルートに `.env` ファイルを作成：

```bash
# OpenAI API設定
OPENAI_API_KEY=your-api-key-here

# Django設定（本番環境用）
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# データベース設定（PostgreSQL使用時）
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### 5. OpenAI API設定ファイル

`config.yml` ファイルでOpenAI APIの詳細設定を管理：

```yaml
# config.yml の主要設定
models:
  default: "gpt-4o-mini"  # デフォルトモデル
  available:
    - "gpt-4o"
    - "gpt-4o-mini"
    - "gpt-4.1"
    - "gpt-4.1-mini"

api:
  timeout: 30
  max_retries: 3
  message_limit: 50
```

## 🗄️ データベースセットアップ

### SQLite3（デフォルト）

```bash
# マイグレーション作成
python manage.py makemigrations

# マイグレーション実行
python manage.py migrate

# スーパーユーザー作成
python manage.py createsuperuser
```

### PostgreSQL（Docker使用）

```bash
# PostgreSQLコンテナ起動
cd docker_compose
docker-compose up -d

# データベース接続確認
python manage.py dbshell
```

### MySQL（Docker使用）

```bash
# MySQLコンテナ起動
cd docker_compose
docker-compose -f docker-compose-mysql.yml up -d
```

## 🏃 開発サーバーの起動

```bash
# 開発サーバー起動
python manage.py runserver

# 別のポートで起動
python manage.py runserver 8080

# 全てのネットワークインターフェースで起動
python manage.py runserver 0.0.0.0:8000
```

アクセスURL:
- アプリケーション: http://localhost:8000
- 管理画面: http://localhost:8000/admin/
- API デモ: http://localhost:8000/test_response_demo/

## 🏗️ プロジェクト構造

```
openai_django_jp/
├── django_web_allauth/      # メインDjangoプロジェクト
│   ├── settings.py          # Django設定
│   ├── urls.py              # ルートURL設定
│   └── wsgi.py              # WSGIアプリケーション
│
├── accounts/                # ユーザー認証アプリ
│   ├── models.py            # カスタムユーザーモデル
│   ├── views.py             # 認証ビュー
│   └── templates/           # 認証テンプレート
│
├── todo_task/               # タスク管理アプリ
│   ├── models.py            # タスクモデル
│   ├── views.py             # CRUD操作
│   └── templates/           # タスクテンプレート
│
├── test_response_demo/      # OpenAI API統合デモ
│   ├── views.py             # API呼び出しロジック
│   └── templates/           # デモUI
│
├── helper_api.py            # OpenAI APIヘルパー関数
├── config.yml               # API設定ファイル
├── requirements.txt         # Pythonパッケージ
└── manage.py                # Django管理コマンド
```

## 🔧 Django基本コマンド

### アプリケーション管理

```bash
# 新しいアプリ作成
python manage.py startapp app_name

# 静的ファイル収集（本番環境）
python manage.py collectstatic

# データベースシェル
python manage.py dbshell

# Pythonシェル（Django環境込み）
python manage.py shell
```

### データ管理

```bash
# データのダンプ
python manage.py dumpdata > data.json

# データのロード
python manage.py loaddata data.json

# 特定アプリのデータダンプ
python manage.py dumpdata todo_task > todo_data.json
```

## 🤖 OpenAI API統合

### 基本的な使用方法

```python
# helper_api.py を使用した実装例
from helper_api import OpenAIClient, get_default_messages

# クライアント初期化
client = OpenAIClient()

# デフォルトメッセージ取得
messages = get_default_messages()
messages.append({
    "role": "user",
    "content": "Pythonでフィボナッチ数列を実装してください"
})

# API呼び出し
response = client.create_response(
    input=messages,
    model="gpt-4o-mini"
)
```

### Django Viewでの実装

```python
# views.py での実装例
from django.shortcuts import render
from django.http import JsonResponse
from helper_api import OpenAIClient, ResponseProcessor

def api_demo(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # OpenAI API呼び出し
        client = OpenAIClient()
        messages = [
            {"role": "user", "content": user_input}
        ]
        
        response = client.create_response(
            input=messages,
            model="gpt-4o-mini"
        )
        
        # レスポンス処理
        result = ResponseProcessor.format_response(response)
        texts = ResponseProcessor.extract_text(response)
        
        return JsonResponse({
            'success': True,
            'response': texts[0] if texts else '',
            'tokens': result.get('usage', {})
        })
```

### モデル選択とパラメータ

```python
# 利用可能なモデル
models = [
    "gpt-4o",          # 高性能汎用モデル
    "gpt-4o-mini",     # コスト効率的なモデル
    "gpt-4.1",         # 最新版GPT-4
    "o1",              # 推論特化モデル
    "o3",              # 高度な推論モデル
]

# 温度パラメータ（創造性の制御）
response = client.create_response(
    input=messages,
    model="gpt-4o-mini",
    temperature=0.7,  # 0.0（決定的）〜 2.0（創造的）
    max_tokens=1000   # 最大出力トークン数
)
```

## 🧪 テスト

### 単体テスト実行

```bash
# 全テスト実行
python manage.py test

# 特定アプリのテスト
python manage.py test accounts
python manage.py test todo_task

# 詳細出力付きテスト
python manage.py test --verbosity=2

# カバレッジ測定
coverage run --source='.' manage.py test
coverage report
coverage html  # HTMLレポート生成
```

### テストデータベース

```bash
# テストデータベースを保持
python manage.py test --keepdb

# 並列実行
python manage.py test --parallel
```

## 📊 管理画面のカスタマイズ

### 管理画面へのモデル登録

```python
# admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'due_date', 'completed']
    list_filter = ['completed', 'due_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'due_date'
```

## 🔐 セキュリティ設定

### 本番環境への移行

```python
# settings.py の本番環境設定
import os
from pathlib import Path

# 環境変数から設定読み込み
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# HTTPSの強制
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# セキュリティヘッダー
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```

## 🌐 国際化とローカライゼーション

```python
# settings.py
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 翻訳ファイル生成
# python manage.py makemessages -l ja
# python manage.py compilemessages
```

## 📝 ログ設定

```python
# settings.py のログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'openai_helper': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    },
}
```

## 🚀 デプロイメント

### Gunicorn + Nginx（本番環境）

```bash
# Gunicornインストール
pip install gunicorn

# Gunicorn起動
gunicorn django_web_allauth.wsgi:application --bind 0.0.0.0:8000

# Supervisorで管理
[program:django_app]
command=/path/to/venv/bin/gunicorn django_web_allauth.wsgi:application
directory=/path/to/project
user=www-data
autostart=true
autorestart=true
```

### Docker化

```dockerfile
# Dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "django_web_allauth.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 📚 追加リソース

- [Django公式ドキュメント](https://docs.djangoproject.com/)
- [OpenAI API リファレンス](https://platform.openai.com/docs/)
- [django-allauth ドキュメント](https://django-allauth.readthedocs.io/)

## 🆘 トラブルシューティング

### よくある問題と解決方法

1. **OpenAI APIキーエラー**
   ```bash
   # 環境変数確認
   echo $OPENAI_API_KEY
   # または .env ファイルを確認
   ```

2. **マイグレーションエラー**
   ```bash
   # マイグレーションリセット
   python manage.py migrate --fake-zero
   python manage.py migrate
   ```

3. **静的ファイルが表示されない**
   ```bash
   # 開発環境
   python manage.py runserver --insecure
   # 本番環境
   python manage.py collectstatic --noinput
   ```

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 コントリビュート

プルリクエストは歓迎します。大きな変更の場合は、まずissueを開いて変更内容を議論してください。

---

*最終更新: 2025年9月*