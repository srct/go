"""
WSGI config for go project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if not os.getenv('DOCKER'):
    dotenv.read_dotenv('../.env')

application = get_wsgi_application()
