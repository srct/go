from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random, string


class URL( models.Model ):
    """
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
    """

    owner = models.ForeignKey( User )
    date_created = models.DateTimeField( default=timezone.now() )

    target = models.URLField( max_length = 1000 )
    short = models.CharField( primary_key = True, max_length = 20 )
    clicks = models.IntegerField( default = 0 )
    expires = models.DateTimeField( blank = True, null = True )

    def __unicode__(self):
        return '<URL: %s>' % self.short

    class Meta:
        ordering = ['short']

    @staticmethod
    def generate_valid_short():
        selection = string.ascii_lowercase + string.digits
        tries = 0
        while True:
            short = ''.join(random.choice(selection) for i in range(5))
            try:
                urls = URL.objects.get( short__iexact = short )
                tries += 1
            except URL.DoesNotExist:
                return short
            if tries > 100:
                return None


class RegisteredUser( models.Model ):
    """
    This is simply a wrapper model which, if an object exists, indicates
    that that user is registered.
    """

    username = models.CharField(
        blank = False,
        max_length = 30,
        primary_key = True
    )

    full_name = models.CharField(
        blank = False,
        max_length = 100,
    )

    description = models.TextField( blank=True )

    def __unicode__(self):
        return '<Registered User: %s>' % self.username

