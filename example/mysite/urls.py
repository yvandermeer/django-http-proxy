from django.conf.urls import patterns, include, url
from django.contrib import admin

from httpproxy.views import HttpProxy


urlpatterns = patterns('',
    url(r'^python/(?P<url>.*)$',
            HttpProxy.as_view(base_url='http://python.org/', rewrite=True)),

    url(r'^admin/', include(admin.site.urls)),
)
