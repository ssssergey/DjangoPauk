from django.conf.urls import url
from views import index, list_by_country, details, login

urlpatterns = [
    # url(r'$', index),
    url(r'news/(?P<news_id>\d+)/$', details, name="details"),
    url(r'login/$', login, name="login"),
    url(r'(?P<slug>[\w-]+)/$', list_by_country, name="list_by_country"),



]
