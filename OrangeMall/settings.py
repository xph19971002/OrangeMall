"""

settings配置

"""

import os
import sys

# 获取当前文件的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps添加python扫描的路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 加密
SECRET_KEY = 't^i8)35!x0t!(_vmu71c8aiphzr9uq78wu0el(6ur0f@tr)cxh'

# 测试环境
DEBUG = True

# 允许访问的ip地址设置
ALLOWED_HOSTS = []

# ----------------------------------------------------------------------
#                            app注册配置
# ----------------------------------------------------------------------

# 系统功能模块
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 第三方功能模块
EXT_APPS = [
    'crispy_forms',
    'xadmin',
    'reversion',
]

# 自定义功能模块
CUSTOM_APPS = [
    'apps.main',
    'apps.account',
    'apps.search',
    'apps.detail',
    'apps.list',
    'apps.car',
    'apps.order',
    'apps.pay',
]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由配置文件
ROOT_URLCONF = 'OrangeMall.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 部署有关文件
WSGI_APPLICATION = 'OrangeMall.wsgi.application'

# ----------------------------------------------------------------------
# 数据库配置
# ----------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omdb',
        'POST': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.50.16',
    }
}

# ----------------------------------------------------------------------
#                           用户密码验证配置
# ----------------------------------------------------------------------
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

# 后台语言
LANGUAGE_CODE = 'zh-hans'

# 设置时区
TIME_ZONE = 'Asia/Shanghai'

# 国际化配置,自动转化多个语言
USE_I18N = True
USE_L10N = True
# 不使使用django的时区,使用系统时区
USE_TZ = False

# 静态文件的访问路径
STATIC_URL = '/static/'

# ----------------------------------------------------------------------
#               静态文件配置 不同的app模块创建不同的static
# ----------------------------------------------------------------------
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static'),
    os.path.join(BASE_DIR, 'apps/detail/static'),
    os.path.join(BASE_DIR, 'apps/search/static'),
    os.path.join(BASE_DIR, 'apps/account/static'),
    os.path.join(BASE_DIR, 'apps/car/static'),
    os.path.join(BASE_DIR,'apps/pay/static'),
)

# 指定自定义用户模型所在的位置
AUTH_USER_MODEL = 'main.User'

# 验证登录路径
LOGIN_URL = '/account/login/'

# ----------------------------------------------------------------------
#                              文件上传配置
# ----------------------------------------------------------------------

# 访问多媒体文件的路径
MEDIA_URL = '/media/'
# 上传文件的根路径， 字符类型
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ----------------------------------------------------------------------
#                               缓存的配置
# ----------------------------------------------------------------------

# pip install django-redis
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             # 'PASSWORD':123
#             # 使用线程池管理连接
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     },
#     'session': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         # 缓存地址
#         "LOCATION": "redis://192.168.50.16:6379/3",
#         "OPTIONS": {
#             # 'PASSWORD':123
#             # 使用线程池管理连接
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     },
# }

# ----------------------------------------------------------------------
#                             session配置
# ----------------------------------------------------------------------

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "session"
#
# # session失效的时间 7天
# SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie失效日期（2周） 默认1209600秒


# ----------------------------------------------------------------------
#                               邮件配置
# ----------------------------------------------------------------------

# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True


# ----------------------------------------------------------------------
#                               日志配置
# ----------------------------------------------------------------------
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }

# ----------------------------------------------------------------------
#                             支付宝支付配置
# ----------------------------------------------------------------------

# 支付宝注册应用生成的id
APP_ID = '2016092400583559'
#
# 测试环境下支付网关
PAY_URL_DEV = 'https://openapi.alipaydev.com/gateway.do?'
# 正式开发环境下支付网关
PAY_URL = 'https://openapi.alipay.com/gateway.do'
# 配置私钥
APP_PRIVATE_KEY_STR = open(os.path.join(BASE_DIR,'app_private_key.pem')).read()
# 配置公钥
APP_PUBLIC_KEY_STR =open(os.path.join(BASE_DIR,'app_public_key.pem')).read()
