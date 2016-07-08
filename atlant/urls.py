# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import atlant_main, generate_doc

urlpatterns = [
    url(r'generate_doc/$', generate_doc, name="generate_doc"),
    url(r'$', atlant_main, name="atlant_main"),
]
