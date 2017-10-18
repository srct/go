#!/usr/bin/env python
import os
import sys

if os.environ['GO_ENV'] == 'production':
    settings = "settings.production"
else:
    settings = "settings.local"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
