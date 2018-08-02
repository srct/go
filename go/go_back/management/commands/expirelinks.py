"""
go/commands/expirelinks.py

Remove expired links from the database.
"""
# Django Imports
from django.core.management.base import BaseCommand
from django.utils import timezone

# App Imports
from go_back.models import URL

class Command(BaseCommand):
    """
    Define a new custom django-admin command to remove expired links from the
    database.
    """
    help = 'Removes expired links from the database'

    def handle(self, *args, **options):
        """
        Handle the main component of the django-admin command. Loop
        through a list of all URL objects that have expired (expires field is
        less than or equal [lte] to today's date)
        """
        for expired_url in URL.objects.filter(expires__lte=timezone.now()):
            expired_url.delete()
