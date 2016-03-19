from django.contrib import admin
from go.models import URL, RegisteredUser


class URLAdmin(admin.ModelAdmin):
    list_display = ("target", "short", "owner", "clicks", "date_created", "expires")


class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "organization", "approved")

admin.site.register(URL, URLAdmin)
admin.site.register(RegisteredUser, RegisteredUserAdmin)
