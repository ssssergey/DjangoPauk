# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404

from .models import News, Countries

# Create your views here.
def index(request):
    countries = Countries.objects.order_by("name")
    return render_to_response('index.html', locals())

def list_by_country(request, slug):
    # country = Countries.objects.get(slug=slug)
    country = get_object_or_404(Countries, slug=slug)
    news = News.objects.filter(country=country.name).order_by("-pub_time")
    return render_to_response('list_by_country.html', locals())

def details(request, news_id):
    # news = News.objects.get(id=news_id)
    news = get_object_or_404(News, id=news_id)
    return render_to_response('details.html', locals())