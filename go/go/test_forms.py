"""
Unit test the Go forms.

References:
    - http://stackoverflow.com/a/7304658
"""

# Python stdlib Imports
from datetime import datetime, timedelta

# Django Imports
from django.contrib.auth.models import User
from django.test import TestCase

# App Imports
from .forms import SignupForm, URLForm, EditForm
from .models import URL, RegisteredUser

class URLFormTest(TestCase):
    """
    Test cases for the URL form
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test')


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

    # def test_valid_form_custom(self):
    #     """
    #     Test that form fields are validated correctly given valid data.
    #     """

    #     form_data = {
    #         'target': 'https://srct.gmu.edu',
    #         'short': 'pls',
    #         'expires': 'Custom Date',
    #         'expires_custom': datetime.now() + timedelta(days=1)
    #     }

    #     form = URLForm(data=form_data)
    #     print(form.errors)
    #     self.assertTrue(form.is_valid())

    def test_invalid_target(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': '.gmu.edu',
            'short': 'pls',
            'expires': '1 Day',
            'expires_custom': ''
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_invalid_short(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': 'https://srct.gmu.edu',
            'short': 'test',
            'expires': '1 Day',
            'expires_custom': ''
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_invalid_expires(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': 'https://srct.gmu.edu',
            'short': 'pls',
            'expires': 'None',
            'expires_custom': ''
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_invalid_expires_custom(self):
        """
        Test that form fields are validated correctly given valid data.
        """

        form_data = {
            'target': 'https://srct.gmu.edu',
            'short': 'pls',
            'expires': 'Custom Date',
            'expires_custom': datetime.now() - timedelta(days=1)
        }

        form = URLForm(data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

class EditForm(TestCase):
    """
    Test cases for the edit URL form.

    As currently this form inherits from the URLForm and does not add any fields,
    we cannot test any values. It exists purely for aesthetics.
    """

    def test_django_test(self):
        """
        Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

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
        Test invalid full_name field
        """

        form_data = {
            'full_name': '',
            'organization': 'SRCT',
            'description': 'the big brown fox jumps over the lazy dog',
            'registered': 'True'
        }

        form = SignupForm(request=None, data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_invalid_organization(self):
        """
        Test invalid organization field
        """

        form_data = {
            'full_name': 'David Haynes',
            'organization': '',
            'description': 'the big brown fox jumps over the lazy dog',
            'registered': 'True'
        }

        form = SignupForm(request=None, data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_blank_description(self):
        """
        Test blank description field
        """

        form_data = {
            'full_name': 'David Haynes',
            'organization': 'SRCT',
            'description': '',
            'registered': 'True'
        }

        form = SignupForm(request=None, data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_registered(self):
        """
        Test invalid registered field
        """

        form_data = {
            'full_name': 'David Haynes',
            'organization': 'SRCT',
            'description': 'the big brown fox jumps over the lazy dog',
            'registered': 'False'
        }

        form = SignupForm(request=None, data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())
