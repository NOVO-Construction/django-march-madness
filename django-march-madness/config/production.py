# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
'''
from configurations import values

from .common import Common


class Production(Common):

    # This ensures that Django will be able to detect a secure connection
    # properly on Heroku.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # SECRET KEY
    SECRET_KEY = values.SecretValue(environ_prefix='', environ_name='SECRET_KEY')
    # END SECRET KEY

    # django-secure
    INSTALLED_APPS += (
        'djangosecure',
        'gunicorn',
    )

    # MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is listed first
        'djangosecure.middleware.SecurityMiddleware',
    )

    MIDDLEWARE_CLASSES += Common.MIDDLEWARE_CLASSES
    # END MIDDLEWARE CONFIGURATION

    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    # EMAIL
    EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
    MANDRILL_API_KEY = values.SecretValue(environ_prefix='', environ_name='MANDRILL_API_KEY')

    DEFAULT_FROM_EMAIL = values.Value('django-march-madness <noreply@novoconstruction.com>')
    EMAIL_SUBJECT_PREFIX = values.Value('[django-march-madness] ', environ_name='EMAIL_SUBJECT_PREFIX')
    EMAIL_USE_TLS = True
    # END EMAIL

    # ######### DATABASE CONFIGURATION
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'madness',
            'USER': values.SecretValue(environ_prefix='', environ_name='MYSQL_USER'),
            'PASSWORD': values.SecretValue(environ_prefix='', environ_name='MYSQL_PASSWORD'),
            'HOST': str(values.SecretValue(environ_prefix='', environ_name='MYSQL_HOST')),
            'PORT': '3306',
        }
    }
    # ######### END DATABASE CONFIGURATION

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    # END TEMPLATE CONFIGURATION

    # ######### CACHE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
    # ######### END CACHE CONFIGURATION

    # Your production stuff: Below this line define 3rd party library settings
