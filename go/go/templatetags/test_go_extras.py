# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

# App Imports
from .go_extras import is_registered, is_approved
from go.models import RegisteredUser

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
            Test the is_registered function to see if it gives correct false answers
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
