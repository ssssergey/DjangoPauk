# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotModified
from rest_framework.generics import ListAPIView
from app.models import Countries

from rest_framework import serializers
from rest_framework.decorators import api_view
from cStringIO import StringIO
from datetime import datetime, date, time

from atlant.atlant import get_news_set, create_docx


class AtlantSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)


class AtlantButtonsAPIView(ListAPIView):
    serializer_class = AtlantSerializer

    def get_queryset(self):
        countries = Countries.objects.all().order_by("name")
        for country in countries:
            q, UC_obj = get_news_set(self.request, country.slug)
            country.quantity = q.count()
        # serializer = AtlantSerializer(countries, many=True)
        # return Response(serializer.data)
        return countries


@api_view()
def generate_docx(request):
    # selected_checkboxes = request.POST.getlist('ch_country')
    country = request.GET['name']
    slug = request.GET['slug']
    q, UC_obj = get_news_set(request, slug)
    if q.count() == 0:
        response = HttpResponseNotModified()
        response['Count'] = q.count()
        response['Content-Disposition'] = 'attachment; filename=empty'
        return response
    try:
        UC_obj.last_time = q.order_by('-download_time')[0].download_time
        UC_obj.save()
    except IndexError:
        pass

    document = create_docx(q)

    f = StringIO()
    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=pauk_{:_<10}_{}.docx'.format(slug, datetime.now().strftime(
        '%H.%M_%d.%m.%Y'))
    response['Content-Length'] = length
    response['Count'] = q.count()
    return response

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'countries/$', AtlantButtonsAPIView.as_view(), name="atlant_countries"),
    url(r'generate_docx/$', generate_docx, name='generate_docx')
]
