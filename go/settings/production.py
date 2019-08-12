"""
settings/production.py

Production settings and globals.
"""

# Base Settings Import
from .base import *

# DEBUG mode is used to view more details when errors occur
# Do not have set True in production
DEBUG = False

CAS_SERVER_URL = "https://login.gmu.edu"

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
    },
}
