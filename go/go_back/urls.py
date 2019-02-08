"""
settings/urls.py

The URLs of the project and their associated view that requests are routed to.
"""
# Django Imports
from django.urls import path, include, re_path
from django.contrib import admin

# Third Party
from rest_framework import routers
from cas import views as cas_views

# App Imports
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r"golinks", views.URLViewSet, base_name="golinks")

# This function attempts to import an admin module in each installed
# application. Such modules are expected to register models with the admin.
admin.autodiscover()

urlpatterns = [
    # Root API URL
    path("api/", include(ROUTER.urls)),
    # Authentication URLs
    path("auth/login/", cas_views.login, name="cas_login"),
    path("auth/logout/", cas_views.logout, name="cas_logout"),
    path("auth/token/", views.CustomAuthToken.as_view()),
    path("auth/status/", views.GetSessionInfo.as_view()),
    # /admin - Administrator interface.
    path("admin/", admin.site.urls, name="go_admin"),
    # Redirection regex.
    re_path(
        r"^(?P<short>([\U00010000-\U0010ffff][\U0000200D]?)+)$",
        views.redirection,
        name="redirection",
    ),
    re_path(r"^(?P<short>[-\w]+)$", views.redirection, name="redirection"),
]
