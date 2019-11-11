"""
go/test_views.py

References:
    - http://stackoverflow.com/a/11887308
"""

# Django Imports
from django.contrib.auth.models import User
from django.test import TestCase, Client

# App Imports
from .models import URL, RegisteredUser

class IndexTest(TestCase):
    """
    Test cases for the index view
    """

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
    """
    Test cases for the new_link view
    """

    def test_new_link_get_anon(self):
        """
        Test that the index view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/newLink')
        self.assertEqual(response.status_code, 302)

class MyLinksTest(TestCase):
    """
    Test cases for the my_links view
    """

    def test_new_link_get_anon(self):
        """
        Test that the index view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/myLinks')
        self.assertEqual(response.status_code, 302)

class PostTest(TestCase):
    """
    Test cases for the post() helper function
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
    """
    Test cases for the edit view
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        # Setup a blank URL object with an owner
        self.user = User.objects.create(username='dhaynes')
        self.user.set_password('test')
        self.user.save()
        ru = RegisteredUser.objects.get(user=self.user)
        URL.objects.create(owner=ru, short='test', target='https://google.com')

    def test_edit_get_anon(self):
        """
        Test that the delete view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/edit/test')
        self.assertEqual(response.status_code, 302)

    def test_edit_get_authed(self):
        c = Client()
        self.assertTrue(c.login(username='dhaynes', password='test'))
        response = c.get('/edit/test')
        self.assertEqual(response.status_code, 200)

    def test_deletes_old_link(self):
        c = Client()
        self.assertTrue(c.login(username='dhaynes', password='test'))
        c.post('/edit/test', {'short': 'newtest', 'target': 'https://google.com', 'expires': 'Never'})
        self.assertEqual(0, URL.objects.filter(short='test').count())
        self.assertEqual(1, URL.objects.filter(short='newtest').count())

    def test_wrong_user(self):
        u = User.objects.create(username='zwood2')
        u.set_password('test')
        u.save()

        c = Client()
        self.assertTrue(c.login(username='zwood2', password='test'))
        response = c.get('/edit/test')
        self.assertEqual(403, response.status_code)

class DeleteTest(TestCase):
    """
    Test cases for the delete view
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        self.user = User.objects.create(username='dhaynes')
        self.user.set_password('test')
        self.user.save()
        ru = RegisteredUser.objects.get(user=self.user)
        URL.objects.create(owner=ru, short='test', target='https://google.com')

    def test_delete_get_anon(self):
        """
        Test that the delete view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/delete/test')
        self.assertEqual(response.status_code, 302)

    def test_deletes_link(self):
        c = Client()
        self.assertTrue(c.login(username='dhaynes', password='test'))
        self.assertEqual(1, URL.objects.filter(short='test').count())
        c.get('/delete/test')
        self.assertEqual(0, URL.objects.filter(short='test').count())

    def test_wrong_user(self):
        u = User.objects.create(username='zwood2')
        u.set_password('test')
        u.save()

        c = Client()
        self.assertTrue(c.login(username='zwood2', password='test'))
        response = c.get('/delete/test')
        self.assertEqual(403, response.status_code)


class RedirectionTest(TestCase):
    """
    Test cases for the redirection view
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user, short='test', target='https://srct.gmu.edu')

    def test_redirect_get_anon(self):
        """
        Test that redirection works as intentioned on anon users.
        """

        response = self.client.get('/test')
        self.assertEqual(response.status_code, 302)

class StaffMemberRequiredTest(TestCase):
    """
    Test cases for the staff_member_required() helper function
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

    def test_useradmin_get_anon(self):
        """
        Test that the useradmin view redirects anons to login with cas on an EXTERNAL
        CAS link, so 302 REDIRECT.
        """

        response = self.client.get('/useradmin')
        self.assertEqual(response.status_code, 302)
