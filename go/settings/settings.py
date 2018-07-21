"""
settings/settings.py

Settings that are applied project wide. 
"""
# Python stdlib Imports
import os
import sys

# DEV vs PROD
if os.environ['GO_ENV'] != 'production':
    DEBUG = True
    # dummy cache for development-- doesn't actually cache things
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:
    DEBUG = False
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': 'localhost:6379',
        },
    }

# STANDALONE VARS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# You can generate a secret key from the following link:
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = os.environ['GO_SECRET_KEY']

# Peoplefinder API
PF_URL = "https://api.srct.gmu.edu/peoplefinder/v1/"

# The domains this application will be deployed on
# e.g. Which domains this app should listen to requests from.
ALLOWED_HOSTS = [os.environ['GO_ALLOWED_HOSTS']]

ADMINS = ()
MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# MEDIA/STATIC FILE CONFIGURATION
MEDIA_URL = '/media/'
MEDIA_ROOT = ''
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, 'media/'),
)

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# TEMPLATING
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

# Use the same DB everywhere.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['GO_DB_NAME'],
        'USER': os.environ['GO_DB_USER'],
        'PASSWORD': os.environ['GO_DB_PASSWORD'],
        'HOST': os.environ['GO_DB_HOST'],
        'PORT': os.environ['GO_DB_PORT'],
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cas.middleware.CASMiddleware',
]

ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'go',
    # Third party
    'crispy_forms',
    'cas',
    'rest_framework',
    'rest_framework.authtoken'
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propogate': True
        },
    }
}

"""
CAS Authentication Settings
"""
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)

CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True

CAS_RESPONSE_CALLBACKS = (
    'go.cas_callbacks.create_user',
)

CAS_SERVER_URL = "https://login.gmu.edu"

"""
Mail Settings
"""
EMAIL_HOST = os.environ['GO_EMAIL_HOST']
EMAIL_PORT = os.environ['GO_EMAIL_PORT']
EMAIL_HOST_USER = os.environ['GO_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['GO_EMAIL_HOST_PASSWORD']
EMAIL_FROM = os.environ['GO_EMAIL_FROM']
EMAIL_TO = os.environ['GO_EMAIL_TO']

# Domain used to email to users. See implementation in views.py
# ie. '@gmu.edu'
EMAIL_DOMAIN = os.environ['GO_EMAIL_DOMAIN']

"""
Django Rest Framework Settings
"""
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}
