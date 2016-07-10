from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'all/$', show_all_articles, name="show_all_articles"),
    url(r'countries/$', get_countries, name="get_countries"),
    url(r'article/(?P<news_id>\d+)/$', show_article, name="show_article"),
    # url(r'login/$', login, name="login"),
    url(r'(?P<slug>[\w-]+)/$', show_country_articles, name="list_by_country"),
    # url(r'generate_docx', generate_docx, name="generate_docx"),

]
