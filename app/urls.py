from django.conf.urls import url
from views import login, generate_docx

urlpatterns = [
    # url(r'news/(?P<news_id>\d+)/$', details, name="details"),
    url(r'login/$', login, name="login"),
    # url(r'(?P<slug>[\w-]+)/$', list_by_country, name="list_by_country"),
    # url(r'generate_docx', generate_docx, name="generate_docx"),

]
