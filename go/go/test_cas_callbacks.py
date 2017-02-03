# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.cas_callbacks import pfparse, pfinfo, create_user

"""
    Test cases for the functions in call_callbacks.
"""
class CasCallbacksTest(TestCase):

    """
        Presently enrolled student who has been added to peoplefinder
    """
    def test_pf_peoplefinder_method(self):
        actual = pfinfo('dhaynes3')
        expected = ['David', 'Haynes']
        self.assertEqual(expected, actual)

    """
        Test the parsing method to ensure that first and last names are seperated
        accordingly and correctly.
    """
    def test_pfparse_peoplefinder_method(self):
        actual = pfparse("Haynes, David M")
        expected = ['David', 'Haynes']
        self.assertEqual(expected, actual)

    """
        student no longer in peoplefinder, or who hasn't yet been added
    """
    def test_pfinfo_ldap_method(self):
        actual = pfinfo('lfaraone')
        expected = ['Luke W', 'Faraone']
        self.assertEqual(expected, actual)

    """
        student employees will have their staff info return before their student info
    """
    def test_pfinfo_employee_method(self):
        actual = pfinfo('nander13')
        expected = ['Nicholas', 'Anderson']
        self.assertEqual(expected, actual)

    """
        a name not found for either (should never happen, but gracefully handle anyway)
    """
    def test_pfinfo_dne(self):
        actual = pfinfo('bobama')
        expected = ['', '']
        self.assertEqual(expected, actual)
