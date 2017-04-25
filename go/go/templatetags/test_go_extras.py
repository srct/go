"""
go/templatetags/test_go_extras.py
"""

# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.contrib.auth.models import User
from django.test import TestCase

# App Imports
from .models import RegisteredUser
from .go_extras import is_approved, is_registered

class GoExtrasTest(TestCase):
    """
    Test cases for the template helper functions in go_extras.py
    """

    def setUp(self):
        """
        Create a dummy user to be tested against.
        """

        User.objects.create(username='dhaynes', password='password')

    # is_registered ------------------------------------------------------------

    def test_is_registered_false(self):
        """
        Test the is_registered function to see if it gives correct false
        answers
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.registered = False
        getRegisteredUser.save()

        self.assertFalse(is_registered(getUser))

    def test_is_registered_true(self):
        """
        Test the is_registered function to see if it gives correct true answers
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.registered = True
        getRegisteredUser.save()

        self.assertTrue(is_registered(getUser))

    # is_approved --------------------------------------------------------------

    def test_is_approved_false(self):
        """
        Test the is_registered function to see if it gives correct false answers
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.approved = False
        getRegisteredUser.save()

        self.assertFalse(is_approved(getUser))


    def test_is_approved_true(self):
        """
        Test the is_registered function to see if it gives correct true answers
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.approved = False
        getRegisteredUser.save()

        self.assertFalse(is_approved(getUser))
