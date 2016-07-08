from django.conf.urls import url, include
from django.contrib import admin
from app.views import index
from marketing.sitemap import SITEMAPS
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^app/', include('app.urls', namespace="app")),
    url(r'^api-app/', include('app.api.urls', namespace="api-app")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^atlant/', include('atlant.urls', namespace="atlant")),
    url(r'^api-atlant/', include('atlant.api.urls', namespace="api-atlant")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS}),

]
