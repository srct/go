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
router.register(r'users', views.UserViewSet)
router.register(r'my', views.URLViewSet, base_name="my")
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


#     # / - Homepage url. Cached for 1 second (this is the page you see after
#     # logging in, so having it show as not logged in is strange)
#     path('', cache_page(1)(go.views.index), name='index'),

#     # /view/<short> - View URL data. Cached for 15 minutes
#     re_path(r'^view/(?P<short>([\U00010000-\U0010ffff][\U0000200D]?)+)$',
#             cache_page(60 * 15)(go.views.view), name='view'),
#     re_path(r'^view/(?P<short>[-\w]+)$',
#             cache_page(60 * 15)(go.views.view), name='view'),

#     # /about - About page. Cached for 15 minutes
#     path('about', cache_page(60 * 15)
#          (TemplateView.as_view(template_name='core/about.html')), name='about'),

#     # /signup - Signup page for access. Cached for 15 minutes
#     path('signup', cache_page(60 * 15)(go.views.signup), name='signup'),

#     # /new - Create a new Go Link
#     path('new', go.views.new_link, name='new_link'),

#     # /my - My-Links page, view and review links.
#     path('my', go.views.my_links, name='my_links'),

#     # /edit/<short> - Edit link form
#     path('edit/<slug:short>', go.views.edit, name='edit'),

#     # /delete/<short> - Delete a link, no content display.
#     path('delete/<slug:short>', go.views.delete, name='delete'),

#     # /registered - registration complete page. Cached for 15 minutes
#     path('registered', cache_page(60 * 15)
#          (TemplateView.as_view(template_name='registered.html')), name='registered'),

#     # /manage - user approval interface
#     path('manage', go.views.useradmin, name='useradmin'),

#     # Redirection regex.
#     re_path(r'^(?P<short>([\U00010000-\U0010ffff][\U0000200D]?)+)$',
#             go.views.redirection, name='redirection'),
#     re_path(r'^(?P<short>[-\w]+)$',
#             go.views.redirection, name='redirection'),
]
