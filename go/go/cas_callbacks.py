from django.contrib.auth.models import User
from django.conf import settings

def create_user(tree):

    username = tree[0][0].text
    user, user_created = User.objects.get_or_create(username=username)

    if user_created:
        user.email = "%s@%s" % (username, settings.ORGANIZATION_EMAIL_DOMAIN)
        user.save()

        print("Created user %s!" % username)
