from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handle404 = "error_404"
handle500 = "error_500"

urlpatterns = patterns('go.views',

    # / - Homepage url.
    url(r'^$', 'index', name = 'index'),

    # /view/<short> - View URL data.
    url(r'^view/(?P<short>\w+)$', 'view', name = 'view'),

    # /about - About page.
    url(r'^about/?$', 'about', name = 'about'),

    # /signup - Signup page for access.
    url(r'^signup/?$', 'signup', name = 'signup'),

    # /my - My-Links page, view and review links.
    url(r'^my/?$', 'my_links', name = 'my_links'),

    # /delete/<short> - Delete a link, no content display.
    url(r'^delete/(?P<short>\w+)$', 'delete', name = 'delete'),

    # /registered - registration complete page
    url(r'^registered/?$', 'registered', name = 'registered'),

    # /admin - Administrator interface.
    url(r'^admin/?', include(admin.site.urls)),

    # /useradmin - user approval interface
    url(r'^useradmin/?$', 'useradmin', name='useradmin'),
)

urlpatterns += patterns('django.contrib.auth.views',

    # Auth pages
    url(r'^login$', 'login', {'template_name' : 'login.html'},
        name='go_login'),
    url(r'^logout$', 'logout', {'next_page' : '/'},
        name='go_logout'),
)

urlpatterns += patterns('go.views',
    # Redirection regex.
    url(r'^(?P<short>\w+)$', 'redirection', name = 'redirection'),
)

# Captcha support
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
