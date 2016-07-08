# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from app.models import Countries
from cStringIO import StringIO
from datetime import datetime
from atlant import get_news_set, create_docx
from django.http import HttpResponse, HttpResponseNotModified

# Create your views here.
def atlant_main(request):
    countries = Countries.objects.all().order_by("name")
    for country in countries:
        q, UC_obj = get_news_set(request, country.slug)
        country.quantity = q.count()
        if country.name == u'Латинская Америка':
            country.name = u'Лат. Америка'
        elif country.name == u'ЮгоВосточная Азия':
            country.name = u'Ю.-В. Азия'
        elif country.name == u'Северный Кавказ':
            country.name = u'Сев. Кавказ'
    return render_to_response('atlant/atlant_main.html', locals())


def generate_doc(request):
    # selected_checkboxes = request.POST.getlist('ch_country')
    print 'dddddddddddddddddddddddddddddddddddddd'
    slug = request.GET['slug']
    q, UC_obj = get_news_set(request, slug)
    if q.count() == 0:
        print 'NO ARTICLES!!!'
        response = HttpResponseNotModified()
        response['Count'] = q.count()
        response['Content-Disposition'] = 'attachment; filename=empty'
        return response
    try:
        UC_obj.last_time = q.order_by('-download_time')[0].download_time
        UC_obj.save()
    except IndexError:
        pass
    print q
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
