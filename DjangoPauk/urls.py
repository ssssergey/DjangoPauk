from django.conf.urls import url, include
from django.contrib import admin
from app.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^app/', include('app.urls', namespace="app")),
    url(r'^api/', include('app.api.urls', namespace="api")),
]
