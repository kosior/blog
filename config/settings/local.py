import os

from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('DJANGO_SECRET_KEY', default='123SuperSecretKey')

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS += [
    '127.0.0.1',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'blog',
#         'USER': 'admin',
#         'PASSWORD': 'admin',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(str(ROOT_DIR), 'db.sqlite3'),
    }
}
