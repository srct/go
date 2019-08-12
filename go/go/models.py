"""
go/models.py
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
from django.conf import settings
from django.core.mail import EmailMessage, send_mail

# Other Imports
from hashids import Hashids  # http://hashids.org/python/

# generate the salt and initialize Hashids
HASHIDS = Hashids(
    salt="srct.gmu.edu", alphabet=(string.ascii_lowercase + string.digits)
)

class RegisteredUser(models.Model):
    """
    This is simply a wrapper model for the user object which, if an object
    exists, indicates that that user is registered.
    """

    # Let's associate a User to this RegisteredUser
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
    registered = models.BooleanField(default=True)

    # Are you approved to use Go?
    approved = models.BooleanField(default=True)

    # Is this User Blocked?
    blocked = models.BooleanField(default=False)

    def __str__(self):
        """
        str(RegisteredUser)
        """

        return '<Registered User: %s - Approval Status: %s>' % (
            self.user, self.approved
        )


@receiver(post_save, sender=User)
def handle_regUser_creation(sender, instance, created, **kwargs):
    """
    When a post_save is called on a User object (and it is newly created), this
    is called to create an associated RegisteredUser
    """

    if created:
        RegisteredUser.objects.create(user=instance)
        # Don't send mail for now
        #
        # user_mail = instance.username + settings.EMAIL_DOMAIN
        # send_mail(
        #             'We have received your Go application!',
        #             ######################
        #             'Hey there %s,\n\n'
        #             'The Go admins have received your application and are '
        #             'currently in the process of reviewing it.\n\n'
        #             'You will receive another email when you have been '
        #             'approved.\n\n'
        #             '- Go Admins'
        #             % (str(instance.username)),
        #             ######################
        #             settings.EMAIL_FROM,
        #             [user_mail]
        #         )


class URL(models.Model):
    """
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
    """

    # Who is the owner of this Go link
    owner = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
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
        print(URL)
        """

        return '<Owner: %s - Target URL: %s>' % (
            self.owner.user, self.target
        )

    class Meta:
        """
        metadata for URLs
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
            print(URL.objects.count())
            cache.set("hashids_counter", URL.objects.count())
            print(cache.get("hashids_counter"))
        tries = 1
        while tries < 100:
            try:
                counter = cache.get("hashids_counter")
                if counter is None:
                    short = HASHIDS.encrypt(0)
                else:
                    short = HASHIDS.encrypt(counter)
                tries += 1
                cache.incr("hashids_counter")
                URL.objects.get(short__iexact=short)
            except URL.DoesNotExist as ex:
                print(ex)
                return short
        return None
