# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# App Imports
from go.models import URL, RegisteredUser

# Define what attributes display in the URL Admin
class URLAdmin(admin.ModelAdmin):
    list_display = ("target", "short", "owner", "clicks", "date_created", "expires")

# Define an inline admin descriptor for User model
class RegisteredUserInline(admin.StackedInline):
  model = RegisteredUser
  can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
  inlines = (RegisteredUserInline, )

# Register URLAdmin and modify User to use new UserAdmin
admin.site.register(URL, URLAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
