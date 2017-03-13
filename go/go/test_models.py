# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

# App Imports
from go.models import URL, RegisteredUser

class RegisteredUserTest(TestCase):
    """
        Test cases for the RegisteredUser Model

        - check approval and registration status flipping
        - check blocking
        - check organization field
        - check full name field
    """

    def setUp(self):
        """
            Set up any variables such as dummy objects that will be utilised in
            testing methods
        """

        User.objects.create(username='dhaynes', password='password')

    def test_registereduser_creation(self):
        """
            check if RegisteredUsers are actually made
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertTrue(getRegisteredUser)

    def test_check_str(self):
        """
            check printing
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        expected = '<Registered User: dhaynes - Approval Status: False>'
        actual = str(getRegisteredUser)
        self.assertEqual(expected, actual)

    def test_description_blank(self):
        """
            - add in description (blank)
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertEqual(getRegisteredUser.description, "")

    def test_description_text(self):
        """
            - add in description
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        getRegisteredUser.description = "We're going to build a big beautiful testcase"
        self.assertEqual(getRegisteredUser.description, "We're going to build a big beautiful testcase")


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
