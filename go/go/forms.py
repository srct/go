"""
go/forms.py
"""

# Python stdlib Imports
from datetime import datetime, timedelta

# Django Imports
from django.core.exceptions import ValidationError
from django.forms import (BooleanField, CharField, ChoiceField, DateTimeField,
                          ModelForm, RadioSelect, SlugField, Textarea,
                          TextInput, URLField, URLInput)
from django.utils import timezone
from django.utils.safestring import mark_safe

# App Imports
from .models import URL

class URLForm(ModelForm):
    def clean_target(self):
        """
        Prevent redirect loop links
        """
        # get the entered target link
        target = self.cleaned_data.get('target')
        return target

    # Custom target URL field
    target = URLField(
        required=True,
        label='Long URL (Required)',
        max_length=1000,
        widget=URLInput(attrs={
            'placeholder': 'https://yoursite.com/',
            'class': 'urlinput form-control',
        })
    )

    # short --------------------------------------------------------------------

    def unique_short(value):
        """
        Check to make sure the short url has not been used
        """

        try:
            # if we're able to get a URL with the same short url
            URL.objects.get(short__iexact=value)
        except URL.DoesNotExist as ex:
            return 

        # then raise a ValidationError
        raise ValidationError('Short URL already exists.')

    # Custom short-url field with validators.
    short = SlugField(
        required=False,
        label='Short URL (Optional)',
        widget=TextInput(
            attrs={
                'class': 'urlinput form-control',
            }
        ),
        validators=[unique_short],
        max_length=20,
        min_length=3,
    )

    # expires ------------------------------------------------------------------

    # Define some string date standards
    DAY = '1 Day'
    WEEK = '1 Week'
    MONTH = '1 Month'
    # CUSTOM = 'Custom Date'
    NEVER = 'Never'

    # Define a tuple of string date standards to be used as our date choices
    EXPIRATION_CHOICES = (
        (DAY, DAY),
        (WEEK, WEEK),
        (MONTH, MONTH),
        (NEVER, NEVER),
        # (CUSTOM, CUSTOM),
    )

    # Add preset expiration choices.
    expires = ChoiceField(
        required=True,
        label='Expiration (Required)',
        choices=EXPIRATION_CHOICES,
        initial=NEVER,
        widget=RadioSelect(attrs={'class': 'radios'}),
    )

    def valid_date(value):
        """
        Check if the selected date is a valid date
        """

        # a valid date is one that is greater than today
        if value > timezone.now():
            return
        # raise a ValidationError if the date is invalid
        else:
            raise ValidationError('Date must be after today.')

    def __init__(self, *args, **kwargs):
        """
        On initialization of the form, crispy forms renders this layout
        """

        # Grab that host info
        self.host = kwargs.pop('host', None)
        super(URLForm, self).__init__(*args, **kwargs)

        self.target_title = 'Paste the URL you would like to shorten:'
        self.short_title = 'Create a custom Go address:'
        self.expires_title = 'Set when you would like your Go address to expire:'

    class Meta:
        """
        Metadata about this ModelForm
        """

        # what model this form is for
        model = URL
        # what attributes are included
        fields = ['target']

class EditForm(URLForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        self.target_title = 'Modify the URL you would like to shorten:'
        self.short_title = 'Modify the Go address:'
        self.expires_title = 'Modify the expiration date:'
