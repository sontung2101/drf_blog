from config.default_settings import *
from datetime import timedelta
AUTH_USER_MODEL = "adminBlog.myUser"

# Django rest framework settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication', #xác thực dùng sesstion
        'rest_framework.authentication.BasicAuthentication', #xacs thực basic gửi user pass qua headẻr
    ),
    #render dữ liệu theo kiểu mình muốn
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': (
        'utils.renderers.EmberJSONRenderer',
    ),
    #setting basic
    'DATETIME_FORMAT': '%d-%m-%Y %H:%M:%S',
    'DATE_FORMAT': '%d-%m-%Y',
    'TIME_FORMAT': '%H:%M:%S',
    'EXCEPTION_HANDLER': 'utils.error.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'utils.paginations.CustomPagination',
    'PAGE_SIZE': 3,
}

#SIMPLE_JWT thay đổi formet gửi Authoiation -> JWT
SIMPLE_JWT = {
    # 'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
}

# DJOSER = {
#     'PASSWORD_RESET_CONFIRM_URL': '/password/reset/confirm/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL': '/username/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL': True,
#     'SERIALIZERS': {
#     },
#
# }
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'sontung2101@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
