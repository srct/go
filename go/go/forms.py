from django import forms
from go.models import URL, RegisteredUser
from django.core.validators import RegexValidator  # MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class URLForm(forms.ModelForm):

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
        required=True,
        label='Expiration',
        choices=EXPIRATION_CHOICES,
        initial=NEVER,
        widget=forms.RadioSelect(),
    )

    def unique_short(value):
        try:
            URL.objects.get(short__iexact=value)
        except URL.DoesNotExist:
            return
        raise ValidationError('Short url already exists.')

    # Custom short-url field with validators.
    short = forms.SlugField(
        required=False,
        label='Short URL (Optional)',
        widget=forms.TextInput(attrs={}),
        validators=[unique_short],
        max_length=20,
        min_length=3,
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


class SignupForm(forms.ModelForm):

    def validate_username(username):
        try:
            registered = RegisteredUser.objects.get(username=username)
            raise ValidationError('Username "%s" is already in use.' % username)
        except RegisteredUser.DoesNotExist:
            return

    username = forms.CharField(
        required=True,
        label='Mason NetID',
        max_length=30,
        validators=[validate_username],
        widget=forms.TextInput(attrs={
        }),
    )
    full_name = forms.CharField(
        required=True,
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(attrs={
        }),
    )
    description = forms.CharField(
        required=False,
        label='Description (Optional)',
        max_length=200,
        widget=forms.Textarea(attrs={
        }),
    )
    captcha = CaptchaField()

    class Meta:
        model = RegisteredUser
        fields = '__all__'
