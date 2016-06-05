from django.conf.urls import url
from views import select_country, generate_docx

urlpatterns = [
    # url(r'$', index),
    url(r'select_country$', select_country, name="select_country"),
    url(r'generate_docx', generate_docx, name="generate_docx"),

]
