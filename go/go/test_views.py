"""
go/test_views.py

Test Go's controller logic.

References:
    - http://stackoverflow.com/a/11887308
"""
# Django Imports
from django.contrib.auth.models import User
from django.test import TestCase, Client

# App Imports
from .models import URL, RegisteredUser

class IndexTest(TestCase):
    def test_index_get_anon(self):
        """
        Test that the index view loads (200 OK) for anons
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_get_auth(self):
        """
        Test that the index view loads (200 OK) for authed users
        """
        client = Client()
        client.login(username='dhaynes', password='password')
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

class NewLinkTest(TestCase):
    def test_new_link_get_anon(self):
        """
        Test that the index view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """
        response = self.client.get('/new')
        self.assertEqual(response.status_code, 302)

class MyLinksTest(TestCase):
    def test_new_link_get_anon(self):
        """
        Test that the index view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """
        response = self.client.get('/my')
        self.assertEqual(response.status_code, 302)

class PostTest(TestCase):
    def test_django_test(self):
        """
        Default test case, does not actually test anything
        """
        self.assertEqual("Hello World!", "Hello World!")

class ViewTest(TestCase):
    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """
        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test')

    def test_view_get_anon(self):
        """
        Test that the view Go link view loads (200 OK) for anon users
        """
        response = self.client.get('/view/test')
        self.assertEqual(response.status_code, 200)

class EditTest(TestCase):
    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """
        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test')

    def test_edit_get_anon(self):
        """
        Test that the delete view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/edit/test')
        self.assertEqual(response.status_code, 302)


class DeleteTest(TestCase):
    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """
        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test')

    def test_delete_get_anon(self):
        """
        Test that the delete view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """
        response = self.client.get('/delete/test')
        self.assertEqual(response.status_code, 302)

class SignupTest(TestCase):
    def test_signup_get_anon(self):
        """
        Test that the signup view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 302)

class RedirectionTest(TestCase):
    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """
        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test', destination='https://srct.gmu.edu')

    # def test_redirect_get_anon(self):
    #     """
    #     Test that redirection works as intentioned on anon users.
    #     """
    #     response = self.client.get('/test')
    #     self.assertEqual(response.status_code, 302) TODO

class StaffMemberRequiredTest(TestCase):
    def test_django_test(self):
        """
        Default test case, does not actually test anything
        """
        self.assertEqual("Hello World!", "Hello World!")

class UserAdminTest(TestCase):
    def test_useradmin_get_anon(self):
        """
        Test that the useradmin view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """
        response = self.client.get('/manage')
        self.assertEqual(response.status_code, 302)
