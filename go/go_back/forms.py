"""
go/forms.py

Configure the layout and styling of the Go's forms.
"""
# Django Imports
from django.forms import (BooleanField, CharField, ChoiceField, DateTimeField,
                          ModelForm, RadioSelect, Textarea, TextInput,
                          URLField, URLInput)
from django.utils.safestring import mark_safe
from django.utils import timezone

# Third party imports
from crispy_forms.bootstrap import (Accordion, AccordionGroup, PrependedText,
                                    StrictButton)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Fieldset, Layout


# App Imports
from .models import URL, RegisteredUser
from .validators import regex_short_validator, valid_date

class URLForm(ModelForm):
    """
    The form that is used in URL creation.

    Define custom fields and then render them onto the template.
    """
    # destination -------------------------------------------------------------
    destination = URLField(
        required=True,
        label='Long URL (Required)',
        max_length=1000,
        widget=URLInput(attrs={
            'placeholder': 'https://yoursite.com/'
        })
    )

    # short -------------------------------------------------------------------
    short = CharField(
        required=False,
        label='Short URL (Optional)',
        widget=TextInput(),
        validators=[regex_short_validator],
        max_length=20,
        min_length=1,
    )

    # expires -----------------------------------------------------------------
    DAY = '1 Day'
    WEEK = '1 Week'
    MONTH = '1 Month'
    CUSTOM = 'Custom Date'
    NEVER = 'Never'

    # Define a tuple of string date standards to be used as our date choices
    EXPIRATION_CHOICES = (
        (DAY, DAY),
        (WEEK, WEEK),
        (MONTH, MONTH),
        (NEVER, NEVER),
        (CUSTOM, CUSTOM),
    )

    expires = ChoiceField(
        required=True,
        label='Expiration (Required)',
        choices=EXPIRATION_CHOICES,
        initial=NEVER,
        widget=RadioSelect(),
    )

    expires_custom = DateTimeField(
        required=False,
        label='Custom Date',
        input_formats=['%m-%d-%Y'],
        validators=[valid_date],
        initial=lambda: timezone.now() + timezone.timedelta(days=1)
    )

    def __init__(self, *args, **kwargs):
        # Grab that host info
        self.host = kwargs.pop('host', None)
        super(URLForm, self).__init__(*args, **kwargs)
        # Define the basics for crispy-forms
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        # Some extra vars for form css purposes
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-6'

        # The main "layout" defined
        self.helper.layout = Layout(
            Fieldset('',
                     #######################
                     Accordion(
                         # Step 1: Long URL
                         AccordionGroup('Step 1: Long URL',
                                        Div(
                                            HTML("""
                                <h4>Paste the URL you would like to shorten:</h4>
                                <br />"""),
                                            'destination',
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html'),

                         # Step 2: Short URL
                         AccordionGroup('Step 2: Short URL',
                                        Div(
                                            HTML("""
                                <h4>Create a custom Go address:</h4>
                                <br />"""),
                                            PrependedText(
                                                'short', 'https://go.gmu.edu/', template='crispy/customPrepended.html'),
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html',),

                         # Step 3: Expiration
                         AccordionGroup('Step 3: URL Expiration',
                                        Div(
                                            HTML("""
                                <h4>Set when you would like your Go address to expire:</h4>
                                <br />"""),
                                            'expires',
                                            Field('expires_custom'),
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html'),

                         # FIN
                         template='crispy/accordian.html'),
                     #######################
                     HTML("""
                <br />"""),
                     StrictButton('Shorten', css_class="btn btn-primary btn-md col-md-4", type='submit')))

    class Meta:
        """
        Metadata about this ModelForm
        """
        # what model this form is for
        model = URL
        # what attributes are included
        fields = ['destination']


class EditForm(URLForm):
    """
    The form that is used in editing URLs.

    A modification of the URL creation form... now for editing URLs. Inherit
    custom form fields for DRY purposes.
    """

    def __init__(self, *args, **kwargs):
        """
        On initialization of the form, crispy forms renders this layout.
        """
        # Grab that host info
        self.host = kwargs.pop('host', None)
        super(URLForm, self).__init__(*args, **kwargs)
        # Define the basics for crispy-forms
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        # Some xtra vars for form css purposes
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-1'
        self.helper.field_class = 'col-md-6'

        # The main "layout" defined
        self.helper.layout = Layout(
            Fieldset('',
                     #######################
                     Accordion(
                         # Step 1: Long URL
                         AccordionGroup('Step 1: Long URL',
                                        Div(
                                            HTML("""
                                <h4>Modify the URL you would like to shorten:</h4>
                                <br />"""),
                                            'destination',
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html'),

                         # Step 2: Short URL
                         AccordionGroup('Step 2: Short URL',
                                        Div(
                                            HTML("""
                                <h4>Modify the Go address:</h4>
                                <br />"""),
                                            PrependedText(
                                                'short', 'https://go.gmu.edu/', template='crispy/customPrepended.html'),
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html',),

                         # Step 3: Expiration
                         AccordionGroup('Step 3: URL Expiration',
                                        Div(
                                            HTML("""
                                <h4>Modify the expiration date:</h4>
                                <br />"""),
                                            'expires',
                                            Field('expires_custom',
                                                  template="crispy/customDateField.html"),
                                            style="background: rgb(#F6F6F6);"),
                                        active=True,
                                        template='crispy/accordian-group.html'),

                         # FIN
                         template='crispy/accordian.html'),
                     #######################
                     HTML("""
                <br />"""),
                     StrictButton('Submit Changes', css_class="btn btn-primary btn-md col-md-4", type='submit')))

    class Meta(URLForm.Meta):
        """
        Metadata about this ModelForm
        """
        # what attributes are included
        fields = URLForm.Meta.fields


class SignupForm(ModelForm):
    """
    The form that is used when a user is signing up to be a RegisteredUser
    """
    full_name = CharField(
        required=True,
        label='Full Name (Required)',
        max_length=100,
        widget=TextInput(),
        help_text="We can fill in this field based on information provided by https://peoplefinder.gmu.edu.",
    )

    organization = CharField(
        required=True,
        label='Organization (Required)',
        max_length=100,
        widget=TextInput(),
        help_text="Or whatever \"group\" you would associate with on campus.",
    )

    description = CharField(
        required=False,
        label='Description (Optional)',
        max_length=200,
        widget=Textarea(),
        help_text="Describe what type of links you would intend to create with Go.",
    )

    # A user becomes registered when they agree to the TOS
    registered = BooleanField(
        required=True,
        # ***Need to replace lower url with production URL***
        # ie. go.gmu.edu/about#terms
        label=mark_safe(
            'Do you accept the <a href="about">Terms of Service</a>?'
        ),
        help_text="Esssentially the GMU Responsible Use of Computing policies.",
    )

    def __init__(self, request, *args, **kwargs):
        """
        On initialization of the form, crispy forms renders this layout.
        """
        # Necessary to call request in forms.py, is otherwise restricted to
        # views.py and models.py
        self.request = request
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-6'

        self.helper.layout = Layout(
            Fieldset('',
                     Div(
                         # Place in form fields
                         Div(
                             'full_name',
                             'organization',
                             'description',
                             'registered',
                             css_class='well'),

                         # Extras at bottom
                         StrictButton(
                             'Submit', css_class='btn btn-primary btn-md col-md-4', type='submit'),
                         css_class='col-md-6')))

    class Meta:
        """
        Metadata about this ModelForm
        """
        # what model this form is for
        model = RegisteredUser
        # what attributes are included
        fields = ['full_name', 'organization', 'description', 'registered']