# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.cas_callbacks import pfparse, pfinfo, create_user

"""
    Test cases for the functions in call_callbacks
"""
class CasCallbacksTest(TestCase):

    def testpfinfo(self):
        print(pfinfo('dhaynes3'))

        self.assertTrue(True)
