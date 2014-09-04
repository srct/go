from django import template
from go.models import RegisteredUser
register = template.Library()

@register.filter
def is_registered( user ):
    try:
        registered = RegisteredUser.objects.get( username=user.username )
        return True
    except RegisteredUser.DoesNotExist:
        return False

@register.filter
def is_approved(user):
    try:
        registered = RegisteredUser.objects.get( username=user.username )
        return registered.approved
    except RegisteredUser.DoesNotExist:
        return False 
