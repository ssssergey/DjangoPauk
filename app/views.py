# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from DjangoPauk import settings

from .models import News, Countries, UserCountry


from datetime import datetime, date, time, timedelta

from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
def index(request):
    # User authentication
    uid = request.COOKIES.get('uid')
    if uid:
        try:
            user = User.objects.get(pk=int(uid))
        except User.DoesNotExist:
            user = create_new_user()
            uid = user.id
    else:
        user = create_new_user()
        uid = user.id
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    # countries = Countries.objects.order_by("name")
    response = render_to_response('index.html', {'user': user}, context_instance=RequestContext(request))
    response.set_cookie('uid', uid, max_age=60 * 60 * 24 * 365)
    # countries = Countries.objects.order_by("name")
    return response

def get_countries(request):
    countries = Countries.objects.all().order_by("name")
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
    return render_to_response('app/show_articles_by_country.html', locals())


def show_article(request, news_id):
    # news = News.objects.get(id=news_id)
    article = get_object_or_404(News, id=news_id)
    return render_to_response('app/show_article.html', locals())


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(u'Неправильные данные')
    return render_to_response("login.html", context=RequestContext(request))


def create_new_user():
    '''
    Helper function
    :return: user object
    '''
    user = User.objects.create_user(username=u"Пользователь")
    user.save()
    user.username = u"Пользователь-{}".format(user.id)
    user.save()
    all_countries = Countries.objects.all()
    for country in all_countries:
        a = UserCountry(user=user, country=country, last_time=datetime.combine(date.today(), time()))
        a.save()
    return user

    # def get_str_date_time(datetime_format):
    #     month_names = ['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября',
    #                    'декабря']
    #     month_name = month_names[datetime_format.month - 1]
    #     date_final = '{} {} {} г.'.format(str(datetime_format.day).lstrip("0"),month_name,str(datetime_format.year))
    #     time_final = datetime_format.strftime("%H.%M")
    #     return date_final, time_final


    # return response
