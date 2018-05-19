"""
go/models.py

The core of Go: define the business logic through classes that represent
tables containing structured data in the database.
"""
# Python stdlib Imports
import string

# Django Imports
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Other Imports
from hashids import Hashids  # http://hashids.org/python/

# generate the salt and initialize Hashids
HASHIDS = Hashids(
    salt="srct.gmu.edu", alphabet=(string.ascii_lowercase + string.digits)
)


class RegisteredUser(models.Model):
    """
    This is simply a wrapper model for the User model which, if an object
    exists, indicates that that user is registered.
    """
    # Let's associate a User to this RegisteredUser
    user = models.OneToOneField(User, on_delete="cascade")

    # What is your name?
    full_name = models.CharField(
        blank=False,
        max_length=100,
    )

    # What organization are you associated with?
    organization = models.CharField(
        blank=False,
        max_length=100,
    )

    # Why do you want to use Go?
    description = models.TextField(blank=True)

    # Have you filled out the registration form?
    registered = models.BooleanField(default=False)

    # Are you approved to use Go?
    approved = models.BooleanField(default=False)

    # Is this User Blocked?
    blocked = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of this object.
        """
        return '<Registered User: %s - Approval Status: %s>' % (
            self.user, self.approved
        )


@receiver(post_save, sender=User)
def handle_regUser_creation(sender, instance, created, **kwargs):
    """
    When a post_save is called on a User object (and it is newly created), this
    is called to create an associated RegisteredUser.
    """
    if created:
        RegisteredUser.objects.create(user=instance)


class URL(models.Model):
    """
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
    """
    # Who is the owner of this Go link
    owner = models.ForeignKey(RegisteredUser, on_delete="cascade")
    # When was this link created?
    date_created = models.DateTimeField(default=timezone.now)

    # What is the target URL for this Go link
    target = models.URLField(max_length=1000)
    # What is the actual go link (short url) for this URL
    short = models.SlugField(max_length=20, primary_key=True)

    # how many people have visited this Go link
    clicks = models.IntegerField(default=0)
    # how many people have visited this Go link through the qr code
    qrclicks = models.IntegerField(default=0)
    # how many people have visited the go link through social media
    socialclicks = models.IntegerField(default=0)

    # does this Go link expire on a certain date
    expires = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """
        String representation of this object.
        """
        return '<Owner: %s - Target URL: %s>' % (
            self.owner.user, self.target
        )

    class Meta:
        """
        Meta information for this object.
        """
        # they should be ordered by their short links
        ordering = ['short']

    @staticmethod
    def generate_valid_short():
        """
        legacy method to ensure that generated short URL's are valid
        should be updated to be simpler
        """
        if cache.get("hashids_counter") is None:
            cache.set("hashids_counter", URL.objects.count())
        tries = 1
        while tries < 100:
            try:
                short = HASHIDS.encrypt(cache.get("hashids_counter"))
                tries += 1
                cache.incr("hashids_counter")
                URL.objects.get(short__iexact=short)
            except URL.DoesNotExist as ex:
                print(ex)
                return short
        return None
