# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

# App Imports
from go.models import URL, RegisteredUser

"""
    Test cases for the RegisteredUser Model

    - check if RegisteredUsers are actually made
    - check approval and registration status flipping
    - check blocking
    - check printing
    - add in description
    - check organization field
    - check full name field
    - check print(RegisteredUser)
"""
class RegisteredUserTest(TestCase):

    def setUp(self):
        User.objects.create(username='dhaynes', password='password')

    def test_RegisteredUserCreation(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertTrue(getRegisteredUser)

    def test_checkPrint(self):
        # expected = '<Registered User: %s - Approval Status: %s>' % (self.user, self.approved)
        self.assertTrue(True)

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
