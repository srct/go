# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.cas_callbacks import *

"""
    Test cases for the functions in call_callbacks
"""
class CasCallbacksTest(TestCase):

    """
        Default test case, does not actually test anything
    """
    def test_Django_Test(self):
        self.assertEqual("Hello World!", "Hello World!")
