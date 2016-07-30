from django.test import TestCase
from go.models import URL, RegisteredUser


class URLTestCase(TestCase):

    def test_Django_Test(self):
        self.assertEqual("Hello World!", "Hello World!")
