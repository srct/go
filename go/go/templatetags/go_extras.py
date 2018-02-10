"""
go/templatetags/go_extras.py

Template functions that can be included to help out with rendering correct
data based on the status of the user.
"""
# Django Imports
from django import template

# App Imports
from go.models import RegisteredUser

# To be a valid tag library, the module must contain a module-level variable
# named register that is a template.Library instance, in which all the tags and
# filters are registered.
register = template.Library()

@register.filter
def is_registered(given_user):
    """
    Check if a user is registered.

    given_user: The User object that we are checking to see if they are
    registered or not.
    """
    # try getting the RegisteredUser of the current user
    try:
        getRegisteredUser = RegisteredUser.objects.get(user=given_user)
        # if it works then the user is registered
        return getRegisteredUser.registered
    # This should never happen
    except RegisteredUser.DoesNotExist as ex:
        print(ex)
        # if they don't exist then they are not registered
        return False

@register.filter
def is_approved(given_user):
    """
    Check if a user is approved.

    given_user: The User object that we are checking to see if they are
    approved or not.
    """
    # try getting the RegisteredUser of the current user
    try:
        get_registered_user = RegisteredUser.objects.get(user=given_user)
        # if they exist, return whether or not they are approved (boolean)
        return get_registered_user.approved
    # This should never happen
    except RegisteredUser.DoesNotExist as ex:
        print(ex)
        # if they don't exist then they are not approved
        return False
