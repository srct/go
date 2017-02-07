# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.urls import reverse

# App Imports
from .urls import *

# https://stackoverflow.com/questions/18987051/how-do-i-unit-test-django-urls

"""
    Test cases for the urls
"""
class UrlsTest(TestCase):

    """
        / - Homepage url.
    """
    def test_index(self):
        url = reverse('index')
        self.assertEqual(url, '/')

