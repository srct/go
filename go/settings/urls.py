# Django Imports
from django.conf.urls import patterns, include, url
import django.contrib.auth.views
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

# App Imports
import go.views

admin.autodiscover()

handle404 = TemplateView.as_view(template_name="admin/404.html")
handle500 = TemplateView.as_view(template_name="admin/500.html")

urlpatterns = [
    # / - Homepage url.
    url(r'^$', go.views.index, name='index'),

    # /view/<short> - View URL data.
    url(r'^view/(?P<short>\w+)$', go.views.view, name='view'),

    # /about - About page.
    url(r'^about/?$', TemplateView.as_view(template_name='core/about.html'), name='about'),

    # /signup - Signup page for access.
    url(r'^signup/?$', go.views.signup, name='signup'),

    # /my - My-Links page, view and review links.
    url(r'^myLinks/?$', go.views.my_links, name='my_links'),

    # /delete/<short> - Delete a link, no content display.
    url(r'^delete/(?P<short>\w+)$', go.views.delete, name='delete'),

    # /registered - registration complete page
    url(r'^registered/?$', TemplateView.as_view(template_name='registered.html'), name='registered'),

    # /admin - Administrator interface.
    url(r'^admin/?', admin.site.urls),

    # /useradmin - user approval interface
    url(r'^useradmin/?$', go.views.useradmin, name='useradmin'),
]
if settings.AUTH_MODE.lower() == "ldap":
    urlpatterns += [
        # Auth pages
        url(r'^login$', django.contrib.auth.views.login, {'template_name' : 'core/login.html'}, name='go_login'),
        url(r'^logout$', django.contrib.auth.views.logout, {'next_page': '/'},
            name='go_logout'),
    ]
else:
    urlpatterns += [
        # Auth pages
        url(r'^login$', django.contrib.auth.views.login, name='go_login'),
        url(r'^logout$', django.contrib.auth.views.logout, {'next_page': '/'},
            name='go_logout'),
    ]

urlpatterns += [
    # Redirection regex.
    url(r'^(?P<short>\w+)$', go.views.redirection, name='redirection'),

]
