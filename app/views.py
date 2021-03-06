# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from DjangoPauk import settings

from .models import News, Countries

from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def index(request):
    # countries = Countries.objects.order_by("name")
    response = render_to_response('index.html', {}, context_instance=RequestContext(request))
    # countries = Countries.objects.order_by("name")
    return response


def get_countries(request):
    countries = Countries.objects.all().order_by("name")
    user = request.user
    return render_to_response('app/show_countries.html', locals())


def show_all_articles(request):
    # country = Countries.objects.get(slug=slug)
    articles = News.objects.all().order_by("-pub_time")[:1000]
    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    # generate the pagintor object
    paginator = Paginator(articles, settings.ARTICLES_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    user = request.user
    return render_to_response('app/show_all_articles.html', locals())


def show_country_articles(request, slug):
    # country = Countries.objects.get(slug=slug)
    country = get_object_or_404(Countries, slug=slug)
    articles = News.objects.filter(country=country.name).order_by("-pub_time")[:1000]
    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    # generate the pagintor object
    paginator = Paginator(articles, settings.ARTICLES_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    page_title = country.name
    user = request.user
    return render_to_response('app/show_articles_by_country.html', locals())


def show_article(request, news_id):
    # news = News.objects.get(id=news_id)
    article = get_object_or_404(News, id=news_id)
    user = request.user
    return render_to_response('app/show_article.html', locals())







    # def get_str_date_time(datetime_format):
    #     month_names = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября',
    #                    'декабря']
    #     month_name = month_names[datetime_format.month - 1]
    #     date_final = '{} {} {} г.'.format(str(datetime_format.day).lstrip("0"),month_name,str(datetime_format.year))
    #     time_final = datetime_format.strftime("%H.%M")
    #     return date_final, time_final


    # return response
