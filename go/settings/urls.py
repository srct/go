# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

# App Imports
import go.views

# This function attempts to import an admin module in each installed
# application. Such modules are expected to register models with the admin.
admin.autodiscover()

# Main list of project URL's
urlpatterns = [
    # / - Homepage url. Cached for 1 second (this is the page you see after
    # logging in, so having it show as not logged in is strange)
    url(r'^$', cache_page(1)(go.views.index), name='index'),

    # /view/<short> - View URL data. Cached for 15 minutes
    url(r'^view/(?P<short>[-\w]+)$', cache_page(60*15)(go.views.view), name='view'),

    # /about - About page. Cached for 15 minutes
    url(r'^about/?$', cache_page(60*15)(TemplateView.as_view(template_name='core/about.html')),
        name='about'),

    # /signup - Signup page for access. Cached for 15 minutes
    url(r'^signup/?$', cache_page(60*15)(go.views.signup), name='signup'),

    # /myLinks - My-Links page, view and review links. Cached for 5 seconds
    url(r'^myLinks/?$', cache_page(5)(go.views.my_links), name='my_links'),

    # /delete/<short> - Delete a link, no content display.
    url(r'^delete/(?P<short>[-\w]+)$', go.views.delete, name='delete'),

    # /registered - registration complete page. Cached for 15 minutes
    url(r'^registered/?$', cache_page(60*15)(TemplateView.as_view(template_name='registered.html')),
        name='registered'),

    # /admin - Administrator interface.
    url(r'^admin/?', admin.site.urls, name='go_admin'),

    # /useradmin - user approval interface
    url(r'^useradmin/?$', go.views.useradmin, name='useradmin'),
]

# Handle authentication pages
urlpatterns += [
    # Auth pages
    url(r'^login$', django.contrib.auth.views.login, name='go_login'),
    url(r'^logout$', django.contrib.auth.views.logout, {'next_page': '/'},
        name='go_logout'),
]

urlpatterns += [
    # Redirection regex.
    url(r'^(?P<short>[-\w]+)$', go.views.redirection, name='redirection'),
]
