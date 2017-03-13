# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import DataError

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

    # user ---------------------------------------------------------------------

    def test_registereduser_creation(self):
        """
            check if RegisteredUsers are actually made
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        self.assertTrue(get_registered_user)

    # full_name ----------------------------------------------------------------

    def test_full_name(self):
        """
            check if full_name char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.full_name = "David Haynes"
        get_registered_user.save()

        self.assertEqual(get_registered_user.full_name, "David Haynes")

    def test_full_name_length(self):
        """
            check if full_name char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.full_name = """
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        """
        try:
            get_registered_user.save()
        except DataError as ex:
            self.assertTrue(ex)

    # blank=False is purely form validation related

    # organization -------------------------------------------------------------

    def test_organization(self):
        """
            check if organization char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.organization = "SRCT"
        get_registered_user.save()

        self.assertEqual(get_registered_user.organization, "SRCT")

    def test_organization_length(self):
        """
            check if organization char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.organization = """
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        """

        try:
            get_registered_user.save()
        except DataError as ex:
            self.assertTrue(ex)


    # blank=False is purely form validation related

    # description --------------------------------------------------------------

    def test_description_blank(self):
        """
            - add in description (blank)
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        self.assertEqual(get_registered_user.description, "")

    def test_description_text(self):
        """
            - add in description (text)
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.description = "We're going to build a big beautiful testcase"
        get_registered_user.save()

        self.assertEqual(
            get_registered_user.description,
            "We're going to build a big beautiful testcase"
        )


    # registered ---------------------------------------------------------------

    def test_registered(self):
        """
            test the registered bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.registered = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.registered)

    def test_registered_default(self):
        """
            test the registered bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertFalse(get_registered_user.registered)

    # approved -----------------------------------------------------------------

    def test_approved(self):
        """
            test the approved bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.approved = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.approved)

    def test_approved_default(self):
        """
            test the approved bool default
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertFalse(get_registered_user.approved)

    # blocked ------------------------------------------------------------------

    def test_blocked(self):
        """
            test the blocked bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.blocked = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.blocked)

    def test_approved_default(self):
        """
            test the blocked bool default
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertFalse(get_registered_user.blocked)


    # __str__ ------------------------------------------------------------------

    def test_check_str(self):
        """
            check printing
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        expected = '<Registered User: dhaynes - Approval Status: False>'
        actual = str(get_registered_user)
        self.assertEqual(expected, actual)


class URLTest(TestCase):
    """
        Test cases for the URL Model
    """

    # owner --------------------------------------------------------------------

    # date_created -------------------------------------------------------------

    # target -------------------------------------------------------------------

    # short --------------------------------------------------------------------

    # clicks -------------------------------------------------------------------

    # qrclicks -----------------------------------------------------------------

    # socialclicks -------------------------------------------------------------

    # expires ------------------------------------------------------------------

    # __str__ ------------------------------------------------------------------

    # generate_valid_short -----------------------------------------------------
