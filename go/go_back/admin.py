"""
go/admin.py

Configure the Django admin pages and apply optional formatting.
"""
# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# App Imports
from .models import URL, RegisteredUser


class RegisteredUserInline(admin.StackedInline):
    """
    Allow for RegisteredUsers to be displayed alongside their Django user
    objects.
    """
    model = RegisteredUser
    can_delete = False


class RegUserAdmin(UserAdmin):
    """
    Stick information about RegisteredUsers into its own Admin panel.
    """
    inlines = (RegisteredUserInline, )


# Default ModelAdmin
admin.site.register(URL)
# Define a new User admin
admin.site.unregister(User)
admin.site.register(User, RegUserAdmin)
