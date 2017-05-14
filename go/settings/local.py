"""
settings/local.py

Development settings and globals.
"""

# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Base Settings Import
from .base import *

# DEBUG mode is used to view more details when errors occur
# Do not have set True in production
DEBUG = True

CAS_SERVER_URL = "https://cas.srct.gmu.edu"

# dummy cache for development-- doesn't actually cache things
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
