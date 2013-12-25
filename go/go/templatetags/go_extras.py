from django import template
from go.models import RegisteredUser
register = template.Library()

@register.filter
def is_registered( user ):
    try:
        registered = RegisteredUser.objects.get( user=user )
        return True
    except RegisteredUser.DoesNotExist:
        return False
