"""
go/commands/test_expirelinks.py

Test that the function to expire Go links actually works.
"""
# Python stdlib Imports
from datetime import timedelta

# Django Imports
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

# App Imports
from go_back.models import URL, RegisteredUser

# class ExpireLinksTest(TestCase):
#     def setUp(self):
#         """
#         Set up any variables such as dummy objects that will be utilized in
#         testing methods
#         """
#         # Setup a blank URL object with an owner
#         User.objects.create(username='dhaynes', password='password')
#         get_user = User.objects.get(username='dhaynes')
#         get_registered_user = RegisteredUser.objects.get(user=get_user)
#         URL.objects.create(owner=get_registered_user, short='test')
#         URL.objects.create(owner=get_registered_user, short='test-2')

#         # Get some dates
#         yesterday = timezone.now() - timedelta(days=1)
#         tomorrow = timezone.now() + timedelta(days=1)

#         # Get the URL to apply it to
#         current_url = URL.objects.get(short='test')
#         second_url = URL.objects.get(short='test-2')

#         # Apply the dates
#         current_url.expires = yesterday
#         second_url.expires = tomorrow
#         current_url.save()
#         second_url.save()

#     def test_expirelinks(self):
#         """
#         Make a call to expire Go links and assert that the number of links has
#         been reduced.
#         """
#         call_command('expirelinks')
#         self.assertTrue(len(URL.objects.all()) == 1) TODO
