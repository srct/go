"""
Unit test the Go forms.

References:
    - http://stackoverflow.com/a/7304658
"""

# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Python stdlib Imports
from datetime import datetime, timedelta

# Django Imports
from django.test import TestCase

# App Imports
from go.forms import URLForm, SignupForm

class URLFormTest(TestCase):
    """
    Test cases for the URL form
    """

    def test_valid_form_no_custom(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': 'https://srct.gmu.edu',
            'short': 'pls',
            'expires': '1 Day',
            'expires_custom': ''
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_valid_form_custom(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': 'https://srct.gmu.edu',
            'short': 'pls',
            'expires': 'Custom Date',
            'expires_custom': datetime.now() + timedelta(days=1)
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

class SignupFormTest(TestCase):
    """
    Test cases for the Signup form
    """

    def test_valid_form(self):
        """
        Test that forms are validated correctly given valid data.
        """

        form_data = {
            'full_name': 'David Haynes',
            'organization': 'SRCT',
            'description': 'the big brown fox jumps over the lazy dog',
            'registered': 'True'
        }

        form = SignupForm(request=None, data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_full_name(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

    def test_invalid_organization(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

    def test_invalid_description(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

    def test_invalid_registered(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")
