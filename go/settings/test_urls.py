# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase
from django.urls import reverse, resolve

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
    def test_index_reverse(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    """
        /view/<short> - View URL data.
    """
    def test_view_reverse_chars(self):
        url = reverse('view', args=['dhaynes'])
        self.assertEqual(url, '/view/dhaynes')

    """
        /view/<short> - View URL data.
    """
    def test_view_reverse_ints(self):
        url = reverse('view', args=['123456789'])
        self.assertEqual(url, '/view/123456789')

    """
        /view/<short> - View URL data.
    """
    def test_view_reverse_chars_ints(self):
        url = reverse('view', args=['dhaynes123'])
        self.assertEqual(url, '/view/dhaynes123')

    """
        /view/<short> - View URL data.
    """
    def test_view_reverse_full_slug(self):
        url = reverse('view', args=['dhaynes123_-'])
        self.assertEqual(url, '/view/dhaynes123_-')

    """
        /about - About page.
    """
    def test_about_reverse(self):
        url = reverse('about')
        self.assertEqual(url, '/about')

    """
        /signup - Signup page for access.
    """
    def test_signup_reverse(self):
        url = reverse('signup')
        self.assertEqual(url, '/signup')

    """
        /myLinks - My-Links page, view and review links.
    """
    def test_my_links_reverse(self):
        url = reverse('my_links')
        self.assertEqual(url, '/myLinks')

    """
        /delete/<short> - Delete a link, no content display.
    """
    def test_delete_reverse_chars(self):
        url = reverse('delete', args=['dhaynes'])
        self.assertEqual(url, '/delete/dhaynes')

    """
        /delete/<short> - Delete a link, no content display.
    """
    def test_delete_reverse_ints(self):
        url = reverse('delete', args=['123456789'])
        self.assertEqual(url, '/delete/123456789')

    """
        /delete/<short> - Delete a link, no content display.
    """
    def test_delete_reverse_chars_ints(self):
        url = reverse('delete', args=['dhaynes123'])
        self.assertEqual(url, '/delete/dhaynes123')

    """
        /delete/<short> - Delete a link, no content display.
    """
    def test_delete_reverse_full_slug(self):
        url = reverse('delete', args=['dhaynes123_-'])
        self.assertEqual(url, '/delete/dhaynes123_-')

    """
        /registered - registration complete page
    """
    def test_registered_reverse(self):
        url = reverse('registered')
        self.assertEqual(url, '/registered')

    # The /admin URL is not tested as it is never resolves in source and generally
    # Django yells at you if the admin page breaks

    """
        /useradmin - user approval interface
    """
    def test_useradmin(self):
        url = reverse('useradmin')
        self.assertEqual(url, '/useradmin')

    """
        /login - login portal
    """
    def test_useradmin(self):
        url = reverse('go_login')
        self.assertEqual(url, '/login')

    """
        /logout - logout portal
    """
    def test_useradmin(self):
        url = reverse('go_logout')
        self.assertEqual(url, '/logout')

    """
        /<short> - Redirect to a go link.
    """
    def test_delete_chars(self):
        url = reverse('redirection', args=['dhaynes'])
        self.assertEqual(url, '/dhaynes')

    """
        /<short> - Redirect to a go link.
    """
    def test_delete_ints(self):
        url = reverse('redirection', args=['123456789'])
        self.assertEqual(url, '/123456789')

    """
        /<short> - Redirect to a go link.
    """
    def test_delete_chars_ints(self):
        url = reverse('redirection', args=['dhaynes123'])
        self.assertEqual(url, '/dhaynes123')

    """
        /<short> - Redirect to a go link.
    """
    def test_delete_full_slug(self):
        url = reverse('redirection', args=['dhaynes123_-'])
        self.assertEqual(url, '/dhaynes123_-')
