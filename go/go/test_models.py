# Django Imports
from django.test import TestCase

# App Imports
from go.models import URL, RegisteredUser

"""
    Test cases for the URL Model
"""
class URLTest(TestCase):

    """
        Default test case, does not actually test anything
    """
    def test_Django_Test(self):
        self.assertEqual("Hello World!", "Hello World!")

"""
    Test cases for the RegisteredUser Model
"""
class RegisteredUserTest(TestCase):

    def test_Django_Test(self):
        self.assertEqual(1+1, 2)
