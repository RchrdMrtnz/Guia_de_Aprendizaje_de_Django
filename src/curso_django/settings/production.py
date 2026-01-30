from .base import *

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='example.com', cast=Csv())

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
