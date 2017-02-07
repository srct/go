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

    """
        # /view/<short> - View URL data.
        url(r'^view/(?P<short>[-\w]+)$', go.views.view, name='view'),
    """
    def test_view_chars(self):
        url = reverse('view', args=['dhaynes'])
        self.assertEqual(url, '/view/dhaynes')

    """
        # /view/<short> - View URL data.
        url(r'^view/(?P<short>[-\w]+)$', go.views.view, name='view'),
    """
    def test_view_ints(self):
        url = reverse('view', args=['123456789'])
        self.assertEqual(url, '/view/123456789')

    """
        # /view/<short> - View URL data.
        url(r'^view/(?P<short>[-\w]+)$', go.views.view, name='view'),
    """
    def test_view_chars_ints(self):
        url = reverse('view', args=['dhaynes123'])
        self.assertEqual(url, '/view/dhaynes123')

    """
        # /view/<short> - View URL data.
        url(r'^view/(?P<short>[-\w]+)$', go.views.view, name='view'),
    """
    def test_view_full_slug(self):
        url = reverse('view', args=['dhaynes123_-'])
        self.assertEqual(url, '/view/dhaynes123_-')
