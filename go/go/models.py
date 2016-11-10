# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

# Other Imports
import string
from hashids import Hashids

hashids = Hashids(salt="srct.gmu.edu", alphabet=(string.ascii_lowercase + string.digits))


class RegisteredUser(models.Model):
    """
    This is simply a wrapper model which, if an object exists, indicates
    that that user is registered.
    """

    # Is this User Blocked?
    blocked = models.BooleanField(default=False)

    # Let's associate a User to this RegisteredUser
    user = models.OneToOneField(User)

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

    # print(RegisteredUser)
    def __unicode__(self):
        return '<Registered User: %s - Approval Status: %s>' % (self.user, self.approved)


# When a post_save is called on a User object (and it is newly created), this is
# called to create an associated RegisteredUser
@receiver(post_save, sender=User)
def handle_regUser_creation(sender, instance, created, **kwargs):
    if created:
        RegisteredUser.objects.create(user=instance)


class URL(models.Model):
    """
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
    """

    owner = models.ForeignKey(RegisteredUser)
    date_created = models.DateTimeField(default=timezone.now)

    target = models.URLField(max_length=1000)
    short = models.SlugField(primary_key=True, max_length=20)
    clicks = models.IntegerField(default=0)

    qrclicks = models.IntegerField(default=0)
    socialclicks = models.IntegerField(default=0)

    expires = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '<%s : %s>' % (self.owner.user, self.target)

    class Meta:
        ordering = ['short']

    @staticmethod
    def generate_valid_short():
        if cache.get("hashids_counter") is None:
            cache.set("hashids_counter", URL.objects.count())
        cache.incr("hashids_counter")
        short = hashids.encrypt(cache.get("hashids_counter"))
        tries = 1
        while tries < 100:
            try:
                URL.objects.get(short__iexact=short)
                tries += 1
                cache.incr("hashids_counter")
            except URL.DoesNotExist:
                return short
        return None
