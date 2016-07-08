# -*- coding: utf-8 -*-
from django.conf.urls import url
# from django.http import HttpResponse, HttpResponseNotModified, StreamingHttpResponse
# from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from app.models import News, Countries, UserCountry

# Permissions
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
# Pagination
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import serializers
# from rest_framework.decorators import api_view
# from cStringIO import StringIO
# from datetime import datetime, date, time


class NewsLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 500
    default_limit = 20

# Renderer
from rest_framework.renderers import JSONRenderer


class UTF8CharsetJSONRenderer(JSONRenderer):
    charset = 'utf-8'


# Serializers define the API representation.
class NewsListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-app:detail',
        lookup_field='id'
    )

    class Meta:
        model = News
        fields = ('id', 'url', 'rss', 'title', 'pub_time', 'download_time', 'country', 'link')


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'rss', 'title', 'body', 'pub_time', 'download_time', 'country', 'link')


class CountryNamesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)


# ViewSets define the view behavior.
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-pub_time')
    serializer_class = NewsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', ]
    pagination_class = NewsLimitOffsetPagination
    # renderer_classes = [UTF8CharsetJSONRenderer]


class NewsCountryAPIView(ListAPIView):
    serializer_class = NewsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', ]
    pagination_class = NewsLimitOffsetPagination

    def get_queryset(self):
        country = self.kwargs['country']
        # result = News.objects.filter(country=country)
        result = Countries.objects.get(slug=country).news_set.all()
        return result


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    # renderer_classes = [UTF8CharsetJSONRenderer]




class ContryNamesAPIView(ListAPIView):
    serializer_class = CountryNamesSerializer

    def get_queryset(self):
        countries = Countries.objects.all().order_by("name")
        # serializer = AtlantSerializer(countries, many=True)
        # return Response(serializer.data)
        return countries


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'(?P<id>[\d-]+)/$', NewsDetailAPIView.as_view(), name="detail"),
    url(r'countries/(?P<country>.+)/$', NewsCountryAPIView.as_view(), name="country"),
    url(r'^$', NewsListAPIView.as_view(), name='list'),
    url(r'countrynames/$', ContryNamesAPIView.as_view(), name="get_countries"),
]
