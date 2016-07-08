# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SearchTerm(models.Model):
    q = models.CharField(u'Поисковая фраза', max_length=50)
    search_date = models.DateTimeField(u'Когда искали', auto_now_add=True)
    ip_address = models.GenericIPAddressField(u'IP-адрес')
    user = models.ForeignKey(User, null=True, verbose_name=u'Пользователь')
    tracking_id = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['-search_date']
        verbose_name = u'Поисковый запрос'
        verbose_name_plural = u'Поисковые запросы'

    def __unicode__(self):
        return self.q
