# CLAUDE_JP.md

このファイルは、Claude Code (claude.ai/code) がこのリポジトリのコードを操作する際のガイダンスを提供します。

## プロジェクト概要

これは、django-allauthを使用したユーザー認証とTodoタスク管理システムを含むDjango Webアプリケーションです。プロジェクトは主に日本語で書かれており、Django認証パターンの学習例として機能します。

## 開発環境セットアップ

### 初期セットアップ
```bash
# 依存関係のインストール
pip install -r requirements.txt

# データベースセットアップ（新規開始時はdb.sqlite3を削除）
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### アプリケーションの実行
```bash
# 開発サーバー起動
python manage.py runserver

# サーバーはデフォルトで http://localhost:8000 で実行
# 管理画面: http://localhost:8000/admin/
```

### テスト実行
```bash
# 全テスト実行
python manage.py test

# 特定のアプリのテスト実行
python manage.py test accounts
python manage.py test todo_task

# 特定のテストファイル実行
python manage.py test todo_task.tests.test_models
python manage.py test todo_task.tests.test_views
python manage.py test todo_task.tests.test_forms
```

### データベースオプション
- **デフォルト**: SQLite3（開発用）
- **PostgreSQL**: settings.pyに設定が記載（コメントアウト済み）
- **MySQL**: `docker_compose/` ディレクトリにDocker composeファイルを配置

## アーキテクチャ

### Djangoプロジェクト構造
- **django_web_allauth/**: 設定とルートURL設定を持つメインのDjangoプロジェクトディレクトリ
- **accounts/**: django-allauthを拡張したカスタムユーザー認証アプリ
- **todo_task/**: ユーザー関連付けを持つタスク管理CRUDアプリケーション

### 認証システム
- django-allauthを使用した包括的な認証
- メールベースログイン（settings.pyで設定）
- カスタムユーザーモデル: `accounts.models.CustomUser`
- 新規登録時のメール確認必須
- ログイン試行とサインアップのレート制限設定

### 主要モデル
- **CustomUser**: カスタムマネージャー付き拡張ユーザーモデル
- **Task**: ユーザー関係を持つTodoタスクモデル、タイトル、説明、期限、完了状態をサポート

### テンプレート構造
- **ベーステンプレート**: `templates/` ディレクトリに配置
- **アプリ固有テンプレート**:
  - `templates/accounts/` 認証ビュー用
  - `templates/todo_task/` タスク管理ビュー用
- **Bootstrapスタイリング**: アプリケーション全体で使用

### URL設定
- ルートURLはホームテンプレートを提供
- `/accounts/` - すべてのdjango-allauth認証URL
- `/todo_task/` - タスク管理機能
- `/admin/` - Django管理インターface

## データベース設定

### 設定モジュール
Djangoの設定モジュールは `django_web_allauth.settings` です。

### デフォルトデータベース
SQLite3がデフォルトで使用され、データベースファイル `db.sqlite3` はプロジェクトルートに配置されます。

### 代替データベース
PostgreSQLとMySQLの設定はsettings.pyに記載されていますがコメントアウトされています。簡単なデータベースセットアップ用のDocker composeファイルが `docker_compose/` に提供されています。

## セキュリティ注意事項
- DEBUGは True に設定（開発のみ）
- シークレットキーはハードコード（本番環境では環境変数にすべき）
- DEBUGモードではコンソールメールバックエンドを使用
- ALLOWED_HOSTSは全ホストを受け入れるよう設定（開発のみ）

## 開発メモ
- 言語：日本語（LANGUAGE_CODE = 'ja'）
- タイムゾーン：Asia/Tokyo
- ロギングはコンソールとファイル（`debug.log`）両方に出力するよう設定
- 開発用にdjango-debug-toolbarを含む
- 両アプリの `tests/` ディレクトリにユニットテストが利用可能