### install & migration
・ ------------------------------------------
・ はじめにやること、マイグレーションとスーパーユーザーの作成。
・ ------------------------------------------
```bash
python3 -m venv venv
pip install -r requirements.txt
```
```bash
# setting
PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=openai_django_jp.settings
```
・はじめに、DBとの接続を実施する。
```python
python manage.py makemigrations
python manage.py migrate

# create super user
python manage.py createsuperuser

# run server
python manage.py runserver localhost:8001
```
・ ------------------------------------------
・ テストの実施方法
・ ------------------------------------------
```python
# run test
python manage.py test
```
・ ------------------------------------------
・ テスト・データの作成方法
・ ------------------------------------------
```python
# Fixture
python manage.py loaddata api/init_data/custom_users.json

python manage.py loaddata sns_app/init_data/profiles.json
```
・ ------------------------------------------
・ ライブラリーの一括インストール方法。
・ ------------------------------------------
・ requests.txt 一括インストール。
$ pip install -r requirements.txt
・ パッケージをインストールしたら、requirements.txtを更新する。
・ ------------------------------------------
・ アプリの登録、作成方法。
・ ------------------------------------------
```python
$ python manage.py startapp command_batch

$ python manage.py startapp sns_app
$ python manage.py startapp api
$ python manage.py startapp api_v1
$ python manage.py startapp api_v2 etc
```
