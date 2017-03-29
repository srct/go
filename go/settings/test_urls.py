"""
settings/test_urls.py

References:
    - https://stackoverflow.com/questions/18987051/how-do-i-unit-test-django-urls
"""

# Future Imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Django Imports
from django.test import TestCase
from django.urls import reverse

class UrlsTest(TestCase):
    """
    Test cases for the urls
    """

    def test_index_reverse(self):
        """
        / - Homepage url.
        """

        url = reverse('index')
        self.assertEqual(url, '/')

    def test_view_reverse_chars(self):
        """
        /view/<short> - View URL data.
        """

        url = reverse('view', args=['dhaynes'])
        self.assertEqual(url, '/view/dhaynes')

    def test_view_reverse_ints(self):
        """
        /view/<short> - View URL data.
        """

        url = reverse('view', args=['123456789'])
        self.assertEqual(url, '/view/123456789')

    def test_view_reverse_chars_ints(self):
        """
        /view/<short> - View URL data.
        """

        url = reverse('view', args=['dhaynes123'])
        self.assertEqual(url, '/view/dhaynes123')

    def test_view_reverse_full_slug(self):
        """
        /view/<short> - View URL data.
        """

        url = reverse('view', args=['dhaynes123_-'])
        self.assertEqual(url, '/view/dhaynes123_-')

    def test_about_reverse(self):
        """
        /about - About page.
        """

        url = reverse('about')
        self.assertEqual(url, '/about')

    def test_signup_reverse(self):
        """
        /signup - Signup page for access.
        """

        url = reverse('signup')
        self.assertEqual(url, '/signup')

    def test_my_links_reverse(self):
        """
        /myLinks - My-Links page, view and review links.
        """

        url = reverse('my_links')
        self.assertEqual(url, '/myLinks')

    def test_delete_reverse_chars(self):
        """
        /delete/<short> - Delete a link, no content display.
        """

        url = reverse('delete', args=['dhaynes'])
        self.assertEqual(url, '/delete/dhaynes')

    def test_delete_reverse_ints(self):
        """
        /delete/<short> - Delete a link, no content display.
        """

        url = reverse('delete', args=['123456789'])
        self.assertEqual(url, '/delete/123456789')

    def test_delete_reverse_chars_ints(self):
        """
            /delete/<short> - Delete a link, no content display.
        """

        url = reverse('delete', args=['dhaynes123'])
        self.assertEqual(url, '/delete/dhaynes123')

    def test_delete_reverse_full_slug(self):
        """
        /delete/<short> - Delete a link, no content display.
        """

        url = reverse('delete', args=['dhaynes123_-'])
        self.assertEqual(url, '/delete/dhaynes123_-')

    def test_registered_reverse(self):
        """
        /registered - registration complete page
        """

        url = reverse('registered')
        self.assertEqual(url, '/registered')

    # The /admin URL is not tested as it is never resolves in source and generally
    # Django yells at you if the admin page breaks

    def test_useradmin(self):
        """
        /useradmin - user approval interface
        """

        url = reverse('useradmin')
        self.assertEqual(url, '/useradmin')

    def test_useradmin(self):
        """
        /login - login portal
        """

        url = reverse('go_login')
        self.assertEqual(url, '/login')

    def test_useradmin(self):
        """
        /logout - logout portal
        """

        url = reverse('go_logout')
        self.assertEqual(url, '/logout')

    def test_delete_chars(self):
        """
        /<short> - Redirect to a go link.
        """

        url = reverse('redirection', args=['dhaynes'])
        self.assertEqual(url, '/dhaynes')

    def test_delete_ints(self):
        """
        /<short> - Redirect to a go link.
        """

        url = reverse('redirection', args=['123456789'])
        self.assertEqual(url, '/123456789')

    def test_delete_chars_ints(self):
        """
        /<short> - Redirect to a go link.
        """

        url = reverse('redirection', args=['dhaynes123'])
        self.assertEqual(url, '/dhaynes123')

    def test_delete_full_slug(self):
        """
        /<short> - Redirect to a go link.
        """

        url = reverse('redirection', args=['dhaynes123_-'])
        self.assertEqual(url, '/dhaynes123_-')
