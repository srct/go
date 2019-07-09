"""
go/cas_callbacks.py
"""

# Django Imports
from django.conf import settings
from django.contrib.auth.models import User

def create_user(tree):
    """
    Create a django user based off of the CAS info
    """

    print("Parsing CAS information.")
    try:
        username = tree[0][0].text
        user, user_created = User.objects.get_or_create(username=username)
    except Exception as ex:
        print("CAS callback unsuccessful:", ex)

    try:
        if user_created:
            print("Created user object %s." % username)

            # set and save the user's email
            email_str = "%s%s" % (username, settings.EMAIL_DOMAIN)
            user.email = email_str
            # Password is a required User object field, though doesn't matter for our
            # purposes because all user auth is handled through CAS, not Django's login.
            user.set_password('cas_used_instead')
            user.save()
            print("Added user's email, %s." % email_str)

            user.save()
            print("User object creation process completed.")

        else:
            print("User object already exists.")

        print("CAS callback successful.")
    except Exception as ex:
        print("Unhandled user creation error:", ex)
