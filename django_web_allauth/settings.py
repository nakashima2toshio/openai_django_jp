# django_web_allauth/settings.py
# ポート競合：
# lsof -i :8000
# kill -9 <PID>
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-ksw06fhq)p9#3-lcqvipg91kt5)4+-q(1*4unsn6tz8=o*j@2v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'todo_task',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug_toolbar
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'django_web_allauth.urls'
# 各アプリケーションのテンプレートディレクトリをリストに追加
# TEMPLATES_DIRS = [
#     BASE_DIR / 'accounts' / 'templates',
#     BASE_DIR / 'dashboard' / 'templates',
#     # 他のアプリケーションもここに追加
# ]
# 'DIRS': [os.path.join(BASE_DIR, 'templates')],
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_web_allauth.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'TEST': {
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}
# # PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'OPTIONS': {
#             'options': '-c search_path=drf_schema,public'
#         },
#         'NAME': 'postgres_db',
#         'USER': 'admin',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
#     'TEST': {
#         'NAME': 'test_postgres_db',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'OPTIONS': {
#             'options': '-c search_path=public'
#         },
#         'USER': 'admin',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 以下非推奨
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# sitesフレームワーク用のサイトID
SITE_ID = 1

# ログイン・ログアウト時のリダイレクト先
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# 新しい設定形式（django-allauth 65.9.0対応）
ACCOUNT_LOGIN_METHODS = ['email']  # メールアドレスでのログインを有効化
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']  # サインアップ時の必須フィールド

# ユーザ登録時に確認メールを送信するか(none=送信しない, mandatory=送信する)
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# レート制限設定
ACCOUNT_RATE_LIMITS = {
    'login_failed': '5/5m',         # 5回のログイン失敗を5分間で制限
    'signup': '20/h',               # 1時間で20回のサインアップを制限
}


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PORT = os.getenv('EMAIL_PORT')
    EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS', False))
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = '自分のgmailアドレス'
# EMAIL_HOST_PASSWORD = 'gmailのパスワード'
# EMAIL_USE_TLS = True

LOGGING = {
    # スキーマバージョンは1固定
    'version': 1,
    # すでに作成されているロガーを無効化しないための設定
    'disable_existing_loggers': False,

    # ログの書式設定
    'formatters': {
        # 詳細ログの書式
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        # 簡易ログの書式
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    # ハンドラ
    'handlers': {
        # コンソール出力用のハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        # ファイル出力用のハンドラ
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },

    # ロガー
    'loggers': {
        # djangoフレームワーク用のロガー
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        # myappアプリケーション用のロガー
        'accounts': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#
# DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    'IS_RUNNING_TESTS': True,
}

if not DEBUG or DEBUG_TOOLBAR_CONFIG.get('IS_RUNNING_TESTS'):
    INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'debug_toolbar']
    MIDDLEWARE = [middleware for middleware in MIDDLEWARE if middleware != 'debug_toolbar.middleware.DebugToolbarMiddleware']
