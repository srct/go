from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('go.views',

    # / - Homepage url.
    url(r'^$', 'index', name = 'homepage'),

    # /about - About page.
    url(r'^about/?$', 'about', name = 'about'),

    # /admin - Administrator interface.
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',

    # Auth pages
    url(r'^login$', 'login', {'template_name' : 'login.html'},
        name='website_login'),
    url(r'^logout$', 'logout', {'next_page' : '/'},
        name='website_logout'),
)
