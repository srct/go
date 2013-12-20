from django import forms
from django.forms import ModelForm, TextInput, RadioSelect, URLInput
from go.models import URL
from django.core.validators import MinLengthValidator, MinValueValidator

class URLForm( ModelForm ):

    DAY = '1 Day'
    WEEK = '1 Week'
    MONTH = '1 Month'
    NEVER = 'Never'

    EXPIRATION_CHOICES = (
        (DAY, DAY),
        (WEEK, WEEK),
        (MONTH, MONTH),
        (NEVER, NEVER),
    )

    # Add a custom expiration choice field.
    expires = forms.ChoiceField(
        required = True,
        label = 'Expiration',
        choices = EXPIRATION_CHOICES,
        initial = NEVER,
        widget = RadioSelect(),
    )

    class Meta:
        model = URL
        fields = ('target', 'short')
        exclude = ('owner', 'date_created', 'clicks', 'expires')
        labels = {
            'target': 'Long URL',
            'short': 'Short URL (Optional)',
        }
        widgets = {
            'target': URLInput(attrs={
                'placeholder': 'http://',
            }),
            'short': TextInput(attrs={
            }),
        }
