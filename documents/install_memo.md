#### 目標：　django-allauth + django-rest-auth:

- Web認証とAPI認証の両方を利用する場合の選択肢

  1. django-allauth + django-rest-auth
     1.1 一般的なWebアプリケーションでの使用に最適です。
     1.2 標準的なユーザー認証、ソーシャルログイン、API認証がすべて統合されています。
     1.3 簡単な設定で始められ、豊富なドキュメントとコミュニティサポートがあります。
  2. Django OAuth Toolkit + django-allauth

  - 高度なAPI認証を必要とする場合に適しています。
  - Web認証とAPI認証の機能を別々に構成できます。
  - より複雑な設定が必要ですが、強力なAPI認証機能が提供されます。

#### 参考：URL

- https://note.com/horiday_tech/n/n2bca87d0e7cd

- https://zenn.dev/mom/books/4c7430e6a7b321/viewer/76c6b9
- https://qiita.com/Nats72/items/8709d063dd2066edd62e

##### ドキュメント

- https://docs.allauth.org/en/latest/

#### インストール手順
- pip install django-allauth
- pip freeze >requirements.txt
-
- python manage.py makemigrations
- python manage.py migrate
- settings.pyの追加設定
- pip install django-debug-toolbar

##### 作成画面

- ログイン画面
- サインアップ画面
- パスワード変更画面
- パスワードリセット画面
