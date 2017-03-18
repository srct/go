# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.test import TestCase

# App Imports
from go.views import *

class IndexTest(TestCase):
    """
        Test cases for the index view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class ViewTest(TestCase):
    """
        Test cases for the "view" view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class MyLinksTest(TestCase):
    """
        Test cases for the my_links view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class DeleteTest(TestCase):
    """
        Test cases for the delete view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class SignupTest(TestCase):
    """
        Test cases for the signup view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class RedirectionTest(TestCase):
    """
        Test cases for the redirection view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")

class UserAdminTest(TestCase):
    """
        Test cases for the useradmin view
    """

    def test_django_test(self):
        """
            Default test case, does not actually test anything
        """

        self.assertEqual("Hello World!", "Hello World!")
