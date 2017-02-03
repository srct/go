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
    Helper template function to check if a user is registered.

    givenUser: The User object that we are checking to see if they are registered
    or not.
"""
@register.filter
def is_registered(givenUser):
    # try getting the RegisteredUser of the current user
    try:
        getRegisteredUser = RegisteredUser.objects.get(user=givenUser)
        # if it works then the user is registered
        return getRegisteredUser.registered
    # This should never happen
    except RegisteredUser.DoesNotExist as ex:
        print(ex)
        # if they don't exist then they are not registered
        return False

"""
    Helper template function to check if a user is approved.

    givenUser: The User object that we are checking to see if they are approved
    or not.
"""
@register.filter
def is_approved(givenUser):
    # try getting the RegisteredUser of the current user
    try:
        getRegisteredUser = RegisteredUser.objects.get(user=givenUser)
        # if they exist, return whether or not they are approved (boolean)
        return getRegisteredUser.approved
    # This should never happen
    except RegisteredUser.DoesNotExist as ex:
        print(ex)
        # if they don't exist then they are not approved
        return False
