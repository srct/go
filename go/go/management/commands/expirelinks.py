# Django Imports
from django.core.management.base import BaseCommand
from django.utils import timezone

# App Imports
from go.models import URL

# Define a new custom django-admin command
class Command(BaseCommand):
    # Define help text for this command
    help = 'Removes expired links from the database'

    # The handle function handles the main component of the django-admin command
    def handle(self, *args, **options):
        # Loop through a list of all URL objects that have expired
        # (expires field is less than or equal to today's date)
        for toexpire in URL.objects.filter(expires__lte=timezone.now()):
            # Delete the current URL
            toexpire.delete()
