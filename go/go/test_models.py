# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User

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

    def setUp(self):
        User.objects.create(username='dhaynes', password='password')

    def test_RegisteredUserCreation(self):
        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertTrue(getRegisteredUser)
