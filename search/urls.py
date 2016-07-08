# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^results/$',results,{'template_name': 'search/results.html'}, 'search_results'),
]