"""
go/validators.py

Reusable validators for objects that are intended to be inserted into the Go
database.
"""
# Python stdlib imports
import re

# Django imports
from django.core.exceptions import ValidationError
from django.utils import timezone

def regex_short_validator(value):
    """
    Run the short through our regex validation before insertion into the
    database.
    """
    # http://stackoverflow.com/a/13752628/6762004
    re_emoji = re.compile("^(([\U00010000-\U0010ffff][\U0000200D]?)+)$")
    re_str = re.compile("^([-\w]+)$")
    if not re_emoji.match(value) and not re_str.match(value):
        raise ValidationError("Short url fails regex check.")


def valid_date(value):
    """
    Check if the selected date is a valid date.
    """
    if value < timezone.now():
        raise ValidationError("Date must be after today.")

def unique_short_validator(value):
    """
    Check to make sure the short url has not been used.
    """
    # Circular dependency resolution through a deferred import
    from .models import URL

    if URL.objects.filter(short__iexact=value).count() > 0:
        raise ValidationError("Short url already exists.")
