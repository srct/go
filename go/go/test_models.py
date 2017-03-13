# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

# App Imports
from go.models import URL, RegisteredUser

"""
    Test cases for the RegisteredUser Model

    - check approval and registration status flipping
    - check blocking
    - add in description
    - check organization field
    - check full name field
"""
class RegisteredUserTest(TestCase):

    def setUp(self):
        User.objects.create(username='dhaynes', password='password')
    
    """
        check if RegisteredUsers are actually made
    """
    def test_RegisteredUserCreation(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertTrue(getRegisteredUser)
    
    """
        - check printing
    """
    def test_checkPrint(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        expected = '<Registered User: dhaynes - Approval Status: False>'
        actual = str(getRegisteredUser)
        self.assertEqual(expected, actual)

"""
    Test cases for the URL Model

    - check if URL's are actually created
    - modify clicks (social, qr, normal)
    - check expiration date creation
    - check print function
"""
class URLTest(TestCase):

    """
        Default test case, does not actually test anything
    """
    def test_Django_Test(self):
        self.assertEqual("Hello World!", "Hello World!")
