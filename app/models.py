from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Countries(models.Model):
    slug = models.SlugField(unique=True)
    name = models.TextField(primary_key=True)

    def __unicode__(self):
        return self.name

class News(models.Model):
    rss = models.TextField()
    title = models.TextField()
    body = models.TextField()
    pub_time = models.DateTimeField()
    country = models.ForeignKey(Countries)
    link = models.TextField()

