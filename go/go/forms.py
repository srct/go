from django import forms
from go.models import URL, RegisteredUser
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div, Field, Button
from crispy_forms.bootstrap import StrictButton, FormActions, PrependedText, Accordion, AccordionGroup, Alert

class URLForm(forms.ModelForm):

    # Custom target URL field
    target = forms.URLField(
        required=True,
        label='Long URL',
        max_length=1000,
        widget=forms.URLInput(attrs={
            'placeholder': 'https://'
        })
    )

    # Check to make sure the short url has not been used
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
        widget=forms.TextInput(),
        validators=[unique_short],
        max_length=20,
        min_length=3,
    )

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

    class Meta:
        model = URL
        fields = ('target',)
        exclude = ('owner', 'short', 'date_created', 'clicks', 'expires')



class URLFormTest(forms.ModelForm):

    # Custom target URL field
    target = forms.URLField(
        required=True,
        label='Long URL',
        max_length=1000,
        widget=forms.URLInput(attrs={
        })
    )

    # Check to make sure the short url has not been used
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
        widget=forms.TextInput(),
        validators=[unique_short],
        max_length=20,
        min_length=3,
    )

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

    def __init__(self, *args, **kwargs):
        super(URLFormTest, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-6'


        self.helper.layout = Layout(
            Fieldset(
                '',
                Accordion(
                    AccordionGroup('Step 1: Long URL',
                        Div(
                            HTML("""
                                <h4>Paste the URL you would like to shorten:</h4>
                                <br />
                            """),
                            PrependedText('target',
                            'https:// required',
                            ),
                            style="background: rgb(#F6F6F6);",
                            title="target_url",
                            css_class="first_group",
                        ),
                        css_id='firstCollapse',
                        active=True,
                        template='crispy/accordian-group.html',
                    ),
                    AccordionGroup('Step 2: Short URL',
                        Div(
                            HTML("""
                                <h4>Create a custom Go address:</h4>
                                <br />
                            """),
                            PrependedText('short',
                            'go.gmu.edu/',
                            ),
                            style="background: rgb(#F6F6F6);",
                            title="short_url",
                            css_class="second_group",
                        ),
                        css_id='secondCollapse',
                        active=False,
                        template='crispy/accordian-group.html',
                    ),
                    AccordionGroup('Step 3: URL Expiration',
                        Div(
                            HTML("""
                                <h4>Set when you would like your Go address to expire:</h4>
                                <br />
                            """),
                            'expires',
                            style="background: rgb(#F6F6F6);",
                            title="expires_url",
                            css_class="third_group",
                        ),
                        css_id='thirdCollapse',
                        active=False,
                        template='crispy/accordian-group.html',
                    ),
                    css_id='accordian',
                    template='crispy/accordian.html'
                ),
            HTML("""
                <br />
            """),
            StrictButton('Shorten', css_class="btn-success", type='submit'),
        )
    )


    class Meta:
        model = URL
        fields = ('target',)
        exclude = ('owner', 'short', 'date_created', 'clicks', 'expires')


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

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-md-4'

        self.helper.help_text_inline = True
        self.helper.error_text_inline = False

        self.helper.layout = Layout(
            Alert(content='<strong>Warning!</strong> Best check yo self, you\'re not looking too good.'),
            Fieldset(
                'Tell us your favorite stuff {{ request.user.username }}',
                Accordion(
                    AccordionGroup('First Group',
                        Div(
                            HTML("""
                            <h4>Here you select whether you like the website or not:</h4>
                            """),
                            'like_website',
                            style="background: rgb(#F6F6F6);",
                            title="First Group",
                            css_class="first_group",
                        ),
                    ),
                    AccordionGroup('Second Group',
                        PrependedText('favorite_color',
                            'https://',
                            placeholder="www."
                        ),
                    )
                ),
                Field(
                    HTML("""
                    <br />
                    """),
                    'favorite_number',
                    'favorite_food',
                    HTML("""
                    <p>We use notes to get better, <strong>please help us {{ request.user.username }}</strong></p>
                    """),
                    'notes',
                    css_class="inputfields"),
                ),
            FormActions(
                StrictButton('Success', css_class="btn-success"),
            )
        )
