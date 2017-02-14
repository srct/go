# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

# App Imports
from .go_extras import is_registered, is_approved
from go.models import RegisteredUser


"""
    Test cases for the template helper functions in go_extras.py
"""
class GoExtrasTest(TestCase):

    """
        Create a dummy user to be tested against.
    """
    def setUp(self):
        User.objects.create(username='dhaynes', password='password')

    """
        Test the is_registered function to see if it gives correct false answers
    """
    def test_is_registeredFalse(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.registered = False
        getRegisteredUser.save()

        self.assertFalse(is_registered(getUser))

    """
        Test the is_registered function to see if it gives correct true answers
    """
    def test_is_registeredTrue(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.registered = True
        getRegisteredUser.save()

        self.assertTrue(is_registered(getUser))

    """
        Test the is_registered function to see if it gives correct false answers
    """
    def test_is_approvedFalse(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.approved = False
        getRegisteredUser.save()

        self.assertFalse(is_approved(getUser))


    """
        Test the is_registered function to see if it gives correct true answers
    """
    def test_is_approvedTrue(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)

        getRegisteredUser.approved = False
        getRegisteredUser.save()

        self.assertFalse(is_approved(getUser))
