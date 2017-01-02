# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django import template

# App Imports
from go.models import RegisteredUser

# To be a valid tag library, the module must contain a module-level variable
# named register that is a template.Library instance, in which all the tags and
# filters are registered.
register = template.Library()

"""
    check if a user is registered
"""
@register.filter
def is_registered(user):
    # try getting the RegisteredUser of the current user
    try:
        registered = RegisteredUser.objects.get(username=user.username)
        # if it works then the user is registered
        return True
    except RegisteredUser.DoesNotExist:
        # if they don't exist then they are not registered
        return False

"""
    check if a user is approved
"""
@register.filter
def is_approved(user):
    # try getting the RegisteredUser of the current user
    try:
        registered = RegisteredUser.objects.get(username=user.username)
        # if they exist, return whether or not they are approved (boolean)
        return registered.approved
    except RegisteredUser.DoesNotExist:
        # if they don't exist then they are not approved
        return False
