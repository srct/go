# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.views import *

"""
    Test cases for the index view
"""
class IndexTest(TestCase):

    """
        Default test case, does not actually test anything
    """
    def test_Django_Test(self):
        self.assertEqual("Hello World!", "Hello World!")
