from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('go.views',

    # / - Homepage url.
    url(r'^$', 'index', name = 'index'),

    # /about - About page.
    url(r'^about/?$', 'about', name = 'about'),

    # /signup - Signup page for access.
    url(r'^signup/?$', 'signup', name = 'signup'),

    # /my - My-Links page, view and review links.
    url(r'^my/?$', 'my_links', name = 'my_links'),

    # /delete - Delete a link, no content display.
    url(r'^delete/(?P<short>\w+)$', 'delete', name = 'delete'),

    # /admin - Administrator interface.
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',

    # Auth pages
    url(r'^login$', 'login', {'template_name' : 'login.html'},
        name='go_login'),
    url(r'^logout$', 'logout', {'next_page' : '/'},
        name='go_logout'),
)
