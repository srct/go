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
from hashids import Hashids

"""
Generate the salt and initialize Hashids

Note: the Hashids library already implements several restrictions on character
placement, including repeating or incrementing numbers, or placing curse word
characters adjacent to one another.
"""
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
        "verbose name",
        max_length=100,
        default="",
        help_text=""
    )

    organization = models.CharField(
        "verbose name",
        max_length=100,
        default="",
        help_text=""
    )

    description = models.TextField(
        "verbose name",
        blank=True,
        default="",
        help_text=""
    )

    registered = models.BooleanField(
        "verbose name",
        default=False,
        help_text=""
    )

    approved = models.BooleanField(
        "verbose name",
        default=False,
        help_text=""
    )

    blocked = models.BooleanField(
        "verbose name",
        default=False,
        help_text=""
    )

    def __str__(self):
        return "<Registered User: {0} - Approval Status: {1}>".format(
            self.user, self.approved
        )


@receiver(post_save, sender=User)
def handle_reguser_creation(sender, instance, created, **kwargs):
    """
    When a post_save is called on a User object (and it is newly created), this
    is called to create an associated RegisteredUser.
    """
    if created:
        RegisteredUser.objects.create(user=instance)


class URL(models.Model):
    """
    The representation of a stored URL redirection rule. Each URL has
    attributes that are used for analytic purposes.
    """
    # DAY = '1 Day'
    # WEEK = '1 Week'
    # MONTH = '1 Month'
    # CUSTOM = 'Custom Date'
    # NEVER = 'Never'

    # EXPIRATION_CHOICES = (
    #     (DAY, DAY),
    #     (WEEK, WEEK),
    #     (MONTH, MONTH),
    #     (NEVER, NEVER),
    #     (CUSTOM, CUSTOM),
    # ) TODO

    owner = models.ForeignKey(
        RegisteredUser,
        on_delete="cascade",
        verbose_name="verbose name"
    )

    date_created = models.DateTimeField(
        "verbose name",
        default=timezone.now,
        help_text=""
    )

    date_expires = models.DateTimeField(
        "verbose name",
        blank=True,
        null=True,
        # choices=EXPIRATION_CHOICES, TODO
        # default=NEVER, TODO
        help_text=""
    )

    destination = models.URLField(
        max_length=1000,
        default="https://go.gmu.edu",
        help_text=""
    )

    # TODO Validator for Slug + Emoji
    """
    # http://stackoverflow.com/a/13752628/6762004
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    slug_unicode_re = _lazy_re_compile(r'^[-\w]+\Z')
    slug_re = _lazy_re_compile(r'^[-a-zA-Z0-9_]+\Z')
    """
    short = models.CharField(
        max_length=20,
        unique=True,
        help_text=""
    )

    # TODO Abstract analytics into their own model
    clicks = models.IntegerField(default=0, help_text="")
    qrclicks = models.IntegerField(default=0, help_text="")
    socialclicks = models.IntegerField(default=0, help_text="")

    def __str__(self):
        return '<Owner: %s - Target URL: %s>' % (
            self.owner.user, self.destination
        )

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
