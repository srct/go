# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# App Imports
from go.models import URL, RegisteredUser

"""
    Define what attributes display in the URL Admin
"""
class URLAdmin(admin.ModelAdmin):
    list_display = ("target", "short", "owner", "clicks", "date_created", "expires")

# Register URLAdmin
admin.site.register(URL, URLAdmin)

"""
    Define an inline admin descriptor for User model
"""
class RegisteredUserInline(admin.StackedInline):
    model = RegisteredUser
    can_delete = False

"""
    Define a new User admin
"""
class UserAdmin(UserAdmin):
    # see above class that we defined
    inlines = (RegisteredUserInline, )

# and modify User to use our new UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
