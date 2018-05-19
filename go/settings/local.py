"""
settings/local.py

Local development settings and globals.
"""
from .base import *

# DEBUG mode is used to view more details when errors occur
# Do not have set True in production
DEBUG = True

#CAS_SERVER_URL = "https://cas.srct.gmu.edu/"
CAS_SERVER_URL = "https://login.gmu.edu"

# dummy cache for development-- doesn't actually cache things
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
