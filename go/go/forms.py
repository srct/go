from django import forms
from go.models import URL
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

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

    # Short field must be only letters.
    alphanumeric = RegexValidator(
        r'^[a-zA-Z]*$',
        'Only letters are allowed.'
    )

    # Custom short-url field with validators.
    short = forms.CharField(
        required = False,
        label = 'Short URL (Optional)',
        widget = forms.TextInput(attrs={}),
        validators = [alphanumeric],
        max_length = 20,
        min_length = 3,
    )

    def clean(self):
        """
        Override the default clean method to check if the entered short
        exists, or if none is entered, to generate a new one.
        """

        cleaned_data = super(URLForm, self).clean()
        short = cleaned_data.get('short').strip()

        # If the user has entered a value for short, then verify that it's
        # unique.
        if len(short) > 0:
            try:
                URL.objects.get(short__iexact=short)
            except URL.DoesNotExist:
                return cleaned_data
            raise ValidationError('Short URL already exists.')

        # If the user did not enter a value for short, then attempt to
        # generate a ranomd url. If a random URL cannot be generated in 100
        # attempts, raise an error.
        else:
            short = URL.generate_valid_short()
            if short is None:
                raise ValidationError('Unable to generate identifier. Try again.')
            else:
                # Set the new, randomly generated short value
                cleaned_data['short'] = short
                return cleaned_data

        # This should never happen.
        raise ValidationError('Server error. Try again.')

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


class SignupForm( forms.Form ):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 30,
        widget = forms.TextInput(attrs={
        }),
    )
    full_name = forms.CharField(
        required = True,
        label = 'Full Name',
        max_length = 100,
        widget = forms.TextInput(attrs={
        }),
    )
    description = forms.CharField(
        required = False,
        label = 'Description (Optional)',
        max_length = 200,
        widget = forms.Textarea(attrs={
        }),
    )
