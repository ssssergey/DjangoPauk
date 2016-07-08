# -*- coding: utf-8 -*-
import os
import base64
from models import SearchTerm
from app.models import News
from django.db.models import Q
# from stats import stats

STRIP_WORDS = [u'в', u'и', u'или', u'для', u'по', u'на', u'из', u'с', u'со', u'под']

# session tracking
def tracking_id(request):
    try:
        return request.session['tracking_id']
    except KeyError:
        request.session['tracking_id'] = base64.b64encode(os.urandom(36))
        return request.session['tracking_id']

# store the search text in the database
def store(request, q):
    # if search term is at least three chars long, store in db
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.tracking_id = tracking_id(request)
        term.user = None
        if request.user.is_authenticated():
            term.user = request.user
        term.save()


# get products matching the search text
def find_news(search_text):
    words = _prepare_words(search_text)
    products = News.objects.all()
    results = {}
    results['products'] = []
    # iterate through keywords
    for word in words:
        products = products.filter(Q(title__icontains=word) |
                                   Q(body__icontains=word) )
        results['products'] = products
    return results


# strip out common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]
