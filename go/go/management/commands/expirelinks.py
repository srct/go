from django.core.management.base import BaseCommand
from django.utils import timezone
from go.models import URL


class Command(BaseCommand):
    help = 'Removes expired links from the database'

    def handle(self, *args, **options):
        for toexpire in URL.objects.filter(expires__lte=timezone.now()):
            toexpire.delete()
