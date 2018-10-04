# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *


class ContentAdmin(admin.ModelAdmin):
    list_display = ('video_url','status','movie_unique')
    list_display_links = ('video_url','status','movie_unique')
    search_fields = ('video_url','status','movie_unique')
    list_per_page = 25

admin.site.register(Content,ContentAdmin)
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
