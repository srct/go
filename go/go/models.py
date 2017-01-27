# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

# Other Imports
from hashids import Hashids # http://hashids.org/python/
import string

# generate the salt and initialize Hashids
hashids = Hashids(salt="srct.gmu.edu", alphabet=(string.ascii_lowercase + string.digits))

"""
    This is simply a wrapper model for the user object  which, if an object
    exists, indicates that that user is registered.
"""
@python_2_unicode_compatible
class RegisteredUser(models.Model):

    # Is this User Blocked?
    blocked = models.BooleanField(default = False)

    # Let's associate a User to this RegisteredUser
    user = models.OneToOneField(User)

    # What is your name?
    full_name = models.CharField(
        blank = False,
        max_length = 100,
    )

    # What organization are you associated with?
    organization = models.CharField(
        blank = False,
        max_length = 100,
    )

    # Why do you want to use Go?
    description = models.TextField(blank = True)

    # Have you filled out the registration form?
    registered = models.BooleanField(default = False)

    # Are you approved to use Go?
    approved = models.BooleanField(default = False)

    # print(RegisteredUser)
    def __str__(self):
        return '<Registered User: %s - Approval Status: %s>' % (self.user, self.approved)


# When a post_save is called on a User object (and it is newly created), this is
# called to create an associated RegisteredUser
@receiver(post_save, sender=User)
def handle_regUser_creation(sender, instance, created, **kwargs):
    if created:
        RegisteredUser.objects.create(user=instance)


"""
    This model represents a stored URL redirection rule. Each URL has an
    owner, target url, short identifier, click counter, and expiration
    date.
"""
@python_2_unicode_compatible
class URL(models.Model):

    # Who is the owner of this Go link
    owner = models.ForeignKey(RegisteredUser)
    # When was this link created?
    date_created = models.DateTimeField(default = timezone.now)

    # What is the target URL for this Go link
    target = models.URLField(max_length = 1000)
    # What is the actual go link (short url) for this URL
    short = models.SlugField(max_length = 20, primary_key = True)

    # how many people have visited this Go link
    clicks = models.IntegerField(default = 0)
    # how many people have visited this Go link through the qr code
    qrclicks = models.IntegerField(default = 0)
    # how many people have visited the go link through social media
    socialclicks = models.IntegerField(default = 0)

    # does this Go link expire on a certain date
    expires = models.DateTimeField(blank = True, null = True)

    # print(URL)
    def __str__(self):
        return '<%s : %s>' % (self.owner.user, self.target)

    # metadata for URL's
    class Meta:
        # they should be ordered by their short links
        ordering = ['short']

    # legacy method to ensure that generated short URL's are valid
    # should be updated to be simpler
    @staticmethod
    def generate_valid_short():
        if cache.get("hashids_counter") is None:
            cache.set("hashids_counter", URL.objects.count())
        cache.incr("hashids_counter")
        short = hashids.encrypt(cache.get("hashids_counter"))
        tries = 1
        while tries < 100:
            try:
                URL.objects.get(short__iexact = short)
                tries += 1
                cache.incr("hashids_counter")
            except URL.DoesNotExist as ex:
                return short
        return None
