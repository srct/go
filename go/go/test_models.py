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
    """

    def setUp(self):
        """
            Set up any variables such as dummy objects that will be utilised in
            testing methods
        """

        User.objects.create(username='dhaynes', password='password')
    
    # User

    def test_registereduser_creation(self):
        """
            check if RegisteredUsers are actually made
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertTrue(getRegisteredUser)

    # full_name

    # organization

    # description

    def test_description_blank(self):
        """
            - add in description (blank)
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        self.assertEqual(getRegisteredUser.description, "")

    def test_description_text(self):
        """
            - add in description (text)
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        getRegisteredUser.description = "We're going to build a big beautiful testcase"
        self.assertEqual(getRegisteredUser.description, "We're going to build a big beautiful testcase")


    # registered

    # approved

    # blocked

    # __str__

    def test_check_str(self):
        """
            check printing
        """

        getUser = User.objects.get(username='dhaynes')
        getRegisteredUser = RegisteredUser.objects.get(user=getUser)
        expected = '<Registered User: dhaynes - Approval Status: False>'
        actual = str(getRegisteredUser)
        self.assertEqual(expected, actual)


class URLTest(TestCase):
    """
        Test cases for the URL Model
    """

    # owner

    # date_created

    # target

    # short

    # clicks

    # qrclicks

    # socialclicks

    # expires

    # __str__

    # generate_valid_short