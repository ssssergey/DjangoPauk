# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from app.models import News, Countries

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_time')
    list_filter = ('pub_time','rss', 'country',)
    # date_hierarchy = 'pub_time'
    ordering = ('-pub_time',)
    fields = ('id','title', 'body', 'rss', 'country', 'pub_time', 'download_time')
    # filter_horizontal = ('rss',)
    # raw_id_fields = ('country',)

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    ordering = ('-name',)
    fields = ('name', 'slug')
admin.site.register(News, NewsAdmin)
admin.site.register(Countries, CountriesAdmin)

