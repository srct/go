# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.forms import URLForm, SignupForm

class URLFormTest(TestCase):
    """
    Test cases for the URL form
    """

    def test_django_test(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class SignupForm(TestCase):
    """
    Test cases for the Signup form
    """

    def test_django_test(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")
