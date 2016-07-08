# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Countries(models.Model):
    slug = models.SlugField(unique=True)
    name = models.TextField(primary_key=True)
    users = models.ManyToManyField(User, related_name='countries', through='UserCountry')

    def __unicode__(self):
        return self.name

class News(models.Model):
    rss = models.TextField()
    title = models.TextField()
    body = models.TextField()
    pub_time = models.DateTimeField()
    download_time = models.DateTimeField()
    country = models.ForeignKey(Countries)
    link = models.TextField()

    def get_absolute_url(self):
        return reverse('app:show_article', args=(self.id,))

    class Meta:
        unique_together = ("title", "pub_time")
        ordering = ['-pub_time']

    def __unicode__(self):
        return self.title

class UserCountry(models.Model):
    user = models.ForeignKey(User)
    country = models.ForeignKey(Countries)
    last_time = models.DateTimeField()
    checked = models.BooleanField(default=True)