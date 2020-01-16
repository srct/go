"""
settings/settings.py

Base Settings
"""

# Python stdlib Imports
import os
import sys

# DEV vs PROD
if os.getenv('GO_ENV') != "production":
    DEBUG = True
else:
    DEBUG = False

# STANDALONE VARS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# You can generate a secret key from the following link:
# http://www.miniwebtool.com/django-secret-key-generator/
# export SECRET_KEY=$(dd if=/dev/urandom count=100 | tr -dc "A-Za-z0-9" | fold -w 60 | head -n1 2>/dev/null)
# assert 'SECRET_KEY' in os.environ, 'You need to set the SECRET_KEY enviornment variable!'
SECRET_KEY = os.environ['GO_SECRET_KEY']

# Peoplefinder API
PF_URL = "https://api.srct.gmu.edu/peoplefinder/v1/"

# The domains this application will be deployed on
# e.g. Which domains this app should listen to requests from.
# ALLOWED_HOSTS = ['127.0.0.1']
ALLOWED_HOSTS = [os.environ['GO_ALLOWED_HOSTS']]

ADMINS = ()
MANAGERS = ADMINS

# TIME
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
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
STATIC_ROOT = '/static'
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
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader'
            ],
        }
    }
]

########## DATABASE CONFIGURATION
# Use the same DB everywhere.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["GO_DB_NAME"],
        "USER": os.environ["GO_DB_USER"],
        "PASSWORD": os.environ["GO_DB_PASSWORD"],
        "HOST": os.environ["GO_DB_HOST"],
        "PORT": os.environ["GO_DB_PORT"],
        "OPTIONS": {"charset": "utf8mb4"},
    }
}


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cas.middleware.CASMiddleware',
]

# URL CONF
ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

# APPS
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'go',
    'qrcode',
    'bootstrap_datepicker',
    'cas',
)

# LOGGING
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

# CAS AUTH
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)

CAS_SERVER_URL = os.getenv('GO_CAS_URL', 'https://login.gmu.edu/')
CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True

CAS_RESPONSE_CALLBACKS = (
    'go.cas_callbacks.create_user',
)


"""
Mail Settings
"""
EMAIL_HOST = os.environ["GO_EMAIL_HOST"]
EMAIL_PORT = os.environ["GO_EMAIL_PORT"]
EMAIL_HOST_USER = os.environ["GO_EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["GO_EMAIL_HOST_PASSWORD"]
EMAIL_FROM = os.environ["GO_EMAIL_FROM"]
EMAIL_TO = os.environ["GO_EMAIL_TO"]

# Domain used to email to users. See implementation in views.py
# ie. '@gmu.edu'
EMAIL_DOMAIN = os.environ["GO_EMAIL_DOMAIN"]

SLACK_URL = os.environ.get("GO_SLACK_URL", "")
