import os

from .base import *


DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME'),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
    }
}
