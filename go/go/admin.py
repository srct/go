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

class URLAdmin(admin.ModelAdmin):
    """
    Define what attributes display in the URL Admin
    """
    list_display = ("target", "short", "owner", "clicks", "date_created", "expires")

# Register URLAdmin
admin.site.register(URL, URLAdmin)

class RegisteredUserInline(admin.StackedInline):
    """
    Define an inline admin descriptor for User model
    """
    model = RegisteredUser
    can_delete = False

class UserAdmin(UserAdmin):
    """
    Define a new User admin
    """
    inlines = (RegisteredUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
