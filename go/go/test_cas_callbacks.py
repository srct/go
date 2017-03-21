# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.cas_callbacks import pfparse, pfinfo

class CasCallbacksTest(TestCase):
    """
    Test cases for the functions in call_callbacks.
    """


    def test_pf_peoplefinder_method(self):
        """
        Presently enrolled student who has been added to peoplefinder
        """

        actual = pfinfo('dhaynes3')
        expected = ['David', 'Haynes']
        self.assertEqual(expected, actual)

    def test_pfparse_peoplefinder_method(self):
        """
        Test the parsing method to ensure that first and last names are seperated
        accordingly and correctly.
        """

        actual = pfparse("Haynes, David M")
        expected = ['David', 'Haynes']
        self.assertEqual(expected, actual)

    def test_pfinfo_ldap_method(self):
        """
        student no longer in peoplefinder, or who hasn't yet been added
        """

        actual = pfinfo('lfaraone')
        expected = ['Luke W', 'Faraone']
        self.assertEqual(expected, actual)

    def test_pfinfo_employee_method(self):
        """
        student employees will have their staff info return before their student info
        """

        actual = pfinfo('nander13')
        expected = ['Nicholas', 'Anderson']
        self.assertEqual(expected, actual)

    def test_pfinfo_dne(self):
        """
        a name not found for either (should never happen, but gracefully handle anyway)
        """

        actual = pfinfo('bobama')
        expected = ['', '']
        self.assertEqual(expected, actual)
