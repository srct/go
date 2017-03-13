# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from .expirelinks import *

class ExpireLinksTest(TestCase):
    """
        Test cases for the functions in expirelinks
    """


    def test_Django_Test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")
