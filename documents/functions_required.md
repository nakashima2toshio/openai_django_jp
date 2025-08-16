#### 必要な機能

##### dj-rest-auth 5.0.1 documentation を利用する: とりあえずは、 can be で。

- ログイン画面
- サインアップ画面
- パスワード変更画面
- パスワードリセット画面

##### 実装機能の一覧 tobe

1. ユーザー登録とアクティベーション
2. ログイン/ログアウト
3. Django ユーザーモデルを取得/更新する
4. パスワードの変更
5. 電子メールによるパスワードのリセット
6. ソーシャルメディア認証

##### dj-rest-auth’s documentation

- https://dj-rest-auth.readthedocs.io/en/latest/index.html

###### ----------------------------------------------------

* Dashboard

- signup
- login
- logout
  表1.1 組み込みの認証システムが提供している機能⼀覧

# dj-rest-auth 利用可能なエンドポイント


| 機能                                      | HTTPメソッド | エンドポイント                    |
| ----------------------------------------- | ------------ | --------------------------------- |
| 1. ユーザ登録                             | POST         | /api/auth/registration/           |
| 2. ユーザ認証,</br>token取得              | POST         | /api/auth/login/                  |
| 3. トークンの無効化                       | POST         | /api/auth/logout/                 |
| 4. パスワードリセットリンクをメールで送信 | POST         | /api/auth/password/reset/         |
| 5. 新しいパスワードを設定                 | POST         | /api/auth/password/reset/confirm/ |
| 6. パスワードを変更                       | POST         | /api/auth/password/change/        |
| 7. ユーザー情報を取得                     | GET          | /api/auth/user/                   |
| 8. ユーザー情報を更新                     | PUT          | /api/auth/user/                   |

その他の認証まわりの機能を実装する場合の例


| 機能             | URL パターン       | ビュー/フォームの例         |
| ---------------- | ------------------ | --------------------------- |
| ユーザー登録     | /accounts/signup/  | CreateView/UserCreationForm |
| ユーザー情報変更 | /accounts/profile/ | UpdateView/UserChangeForm   |
