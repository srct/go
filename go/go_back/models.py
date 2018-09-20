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
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Other Imports
from hashids import Hashids
from .validators import regex_short_validator, unique_short_validator
from rest_framework.authtoken.models import Token

# Generate the salt and initialize Hashids
# Note: the Hashids library already implements several restrictions oncharacter
# placement, including repeating or incrementing numbers, or placing curse word
# characters adjacent to one another.
SIMILAR_CHARS = set(['b', 'G', '6', 'g', 'q', 'l',
                     '1', 'I', 'S', '5', 'O', '0'])
ALPHANUMERICS = set(string.ascii_letters + string.digits)
LINK_CHARS = ''.join(ALPHANUMERICS - SIMILAR_CHARS)

HASHIDS = Hashids(
    salt="srct.gmu.edu", alphabet=(LINK_CHARS)
)

class RegisteredUser(models.Model):
    """
    Wrapper model for the built in User model which stores data pertaining to
    the registration / approval / blocked status of a django user.
    """
    user = models.OneToOneField(
        User,
        on_delete="cascade",
        verbose_name="Django User Object"
    )

    full_name = models.CharField(
        "Full Name",
        max_length=100,
        default="",
    )

    organization = models.CharField(
        "Organization",
        max_length=100,
        default="",
    )

    description = models.TextField(
        "Signup Description",
        blank=True,
        default="",
    )

    registered = models.BooleanField(
        "Registration Status",
        default=False,
    )

    approved = models.BooleanField(
        "Approval Status",
        default=False,
    )

    blocked = models.BooleanField(
        "Blocked Status",
        default=False,
    )

    def __str__(self):
        return f"<RegisteredUser: {self.user} - Approval Status: {self.approved}>"

@receiver(post_save, sender=User)
def handle_reguser_creation(sender, instance, created, **kwargs):
    """
    When a post_save is called on a User object (and it is newly created), this
    is called to create an associated RegisteredUser.
    """
    if created:
        RegisteredUser.objects.create(user=instance, full_name=instance.get_full_name())

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print(token.key)

def handle_user_deletion():


class URL(models.Model):
    """
    The representation of a stored URL redirection rule. Each URL has
    attributes that are used for analytic purposes.
    """
    owner = models.ForeignKey(
        RegisteredUser,
        on_delete="cascade",
        verbose_name="RegisteredUser Owner"
    )

    date_created = models.DateTimeField(
        "Go Link Creation Date",
        default=timezone.now,
    )

    date_expires = models.DateTimeField(
        "Go Link Expiry Date",
        blank=True,
        null=True,
    )

    destination = models.URLField(
        "Go Link Destination URL",
        max_length=1000,
        default="https://go.gmu.edu",
    )

    # Note: min_length cannot exist on a model so it is enforced in forms.py
    short = models.CharField(
        "Go Shortcode",
        max_length=20,
        unique=True,
        validators=[unique_short_validator, regex_short_validator],
    )

    # TODO Abstract analytics into their own model
    clicks = models.IntegerField(default=0, help_text="")
    qrclicks = models.IntegerField(default=0, help_text="")
    socialclicks = models.IntegerField(default=0, help_text="")

    def __str__(self):
        return f"<Owner: {self.owner.user} - Destination URL: {self.destination}>"

    class Meta:
        ordering = ['short']

    @staticmethod
    def generate_valid_short():
        """
        Generate a short to be used as a default go link if the user does not
        provide a custom one.
        """
        if cache.get("hashids_counter") is None:
            cache.set("hashids_counter", URL.objects.count())

        short = HASHIDS.encrypt(cache.get("hashids_counter"))

        # Continually generate new shorts until there are no conflicts
        while URL.objects.filter(short__iexact=short).count() > 0:
            short = HASHIDS.encrypt(cache.get("hashids_counter"))

        return short
