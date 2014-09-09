from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import random, string

from hashids import Hashids
hashids = Hashids(salt="srct.gmu.edu", alphabet=(string.ascii_lowercase + string.digits))
hashids_counter = None

class URL( models.Model ):
    """
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
    """

    owner = models.ForeignKey( User )
    date_created = models.DateTimeField( default=timezone.now )

    target = models.URLField( max_length = 1000 )
    short = models.CharField( primary_key = True, max_length = 20 )
    clicks = models.IntegerField( default = 0 )
    expires = models.DateTimeField( blank = True, null = True )



    def __unicode__(self):
        return '<%s : %s>' % (self.owner.username, self.target)

    class Meta:
        ordering = ['short']

    @staticmethod
    def generate_valid_short():
        global hashids_counter
        hashids_counter += 1
        short = hashids.encrypt(hashids_counter)
        tries = 1
        while tries < 100:
            try:
                urls = URL.objects.get( short__iexact = short )
                tries += 1
                hashids_counter += 1
            except URL.DoesNotExist:
                return short
        return None

# this needs to be here instead of at the top because the model's manager must be available before this line
hashids_counter = URL.objects.count()


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

    approved = models.BooleanField()

    def __unicode__(self):
        return '<Registered User: %s - Approval Status: %s>' % (self.username, self.approved)

