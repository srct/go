"""
settings/urls.py

The URLs of the project and their associated view that requests are routed to.
"""
# Django Imports
import django.contrib.auth.views
from django.urls import path, re_path, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

# App Imports
from go import views
from cas import views as cas_views

# Third Party
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'my', views.URLViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'registereduser', views.RegisteredUserViewSet)

# This function attempts to import an admin module in each installed
# application. Such modules are expected to register models with the admin.
admin.autodiscover()

urlpatterns = [
    # Root API URL
    path("", include(router.urls)),

    # Authentication URLs
    path('auth/login/', cas_views.login, name='cas_login'),
    path('auth/logout/', cas_views.logout, {'next_page': '/'}, name='cas_logout'),

    # /admin - Administrator interface.
    path('admin/', admin.site.urls, name='go_admin'),
    path('auth/', include('rest_framework.urls'))


#     # /view/<short> - View URL data. Cached for 15 minutes
#     re_path(r'^view/(?P<short>([\U00010000-\U0010ffff][\U0000200D]?)+)$',
#             cache_page(60 * 15)(go.views.view), name='view'),
#     re_path(r'^view/(?P<short>[-\w]+)$',
#             cache_page(60 * 15)(go.views.view), name='view'),

#     # Redirection regex.
#     re_path(r'^(?P<short>([\U00010000-\U0010ffff][\U0000200D]?)+)$',
#             go.views.redirection, name='redirection'),
#     re_path(r'^(?P<short>[-\w]+)$',
#             go.views.redirection, name='redirection'),
]
