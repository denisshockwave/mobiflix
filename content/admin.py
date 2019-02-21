# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *


class ContentAdmin(admin.ModelAdmin):
    list_display = ('name','status','category','time','genre','stars','director','county','video_qualify','imdb','release','rating')
    list_display_links = ('name','status','time','genre','stars','director','county','video_qualify','imdb','release','rating')
    search_fields = ('name','status','time','genre','stars','director','county','video_qualify','imdb','release','rating')
    list_per_page = 25

admin.site.register(Content,ContentAdmin)

class ContentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links =('name','id')
    search_fields = ('name','id')
    list_per_page = 25

admin.site.register(ContentCategory,ContentCategoryAdmin)


class WatchersAdmin(admin.ModelAdmin):
    list_display = ('unique_code','code_expiration','logged_in_counter','last_login','devices')
    list_display_links = ('unique_code','code_expiration','logged_in_counter','last_login','devices')
    search_fields = ('unique_code','code_expiration','logged_in_counter','last_login','devices')
    list_per_page = 25

admin.site.register(Watchers,WatchersAdmin)

class DevicesAdmin(admin.ModelAdmin):
    list_display = ('device1','device2')
    list_display_links = ('device1','device2')
    search_fields = ('device1','device2')
    list_per_page = 25

admin.site.register(Devices,DevicesAdmin)


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('number', 'id')
    list_display_links = ('number',)
    search_fields = ('number', 'id')
    list_per_page = 25


admin.site.register(Series,SeriesAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('number', 'id','tagline')
    list_display_links = ('number',)
    search_fields = ('number', 'tagline')
    list_per_page = 25


admin.site.register(Episode, EpisodeAdmin)


