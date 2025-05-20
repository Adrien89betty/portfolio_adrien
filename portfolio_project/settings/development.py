from .base import *

# Dev settings
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = []

# Local DB
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD', default=''),
    'HOST': config('DB_HOST', default='localhost'),
    'PORT': config('DB_PORT', default='5432'),
    }
}

# Dev email backend settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Default adress (sending / reception)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_RECIPIENT = config('CONTACT_RECIPIENT', EMAIL_HOST_USER)
