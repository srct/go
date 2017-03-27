"""
go/commands/expirelinks.py
"""

# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


# Django Imports
from django.core.management.base import BaseCommand
from django.utils import timezone

# App Imports
from go.models import URL

class Command(BaseCommand):
    """
    Define a new custom django-admin command to remove expired links from the
    database
    """

    # Define help text for this command
    help = 'Removes expired links from the database'

    def handle(self, *args, **options):
        """
        The handle function handles the main component of the django-admin command.
        """

        # Loop through a list of all URL objects that have expired
        # (expires field is less than or equal to today's date)
        for toexpire in URL.objects.filter(expires__lte=timezone.now()):
            # Delete the current URL
            toexpire.delete()
