from django import forms
from go.models import URL
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator

class URLForm( forms.ModelForm ):

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
        widget = forms.RadioSelect(),
    )

    # Add a custom short field for validation.
    alphanumeric = RegexValidator(
        r'^[a-zA-Z]*$',
        'Only letters are allowed.'
    )
    short = forms.CharField(
        required = False,
        label = 'Short URL (Optional)',
        widget = forms.TextInput(attrs={}),
        validators = [alphanumeric],
        max_length = 20,
        min_length = 3,
    )

    class Meta:
        model = URL
        fields = ('target',)
        exclude = ('owner', 'short', 'date_created', 'clicks', 'expires')
        labels = {
            'target': 'Long URL',
        }
        widgets = {
            'target': forms.URLInput(attrs={
                'placeholder': 'http://',
            }),
        }
