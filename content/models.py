# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
    video_url=models.FileField(upload_to="uploads",null=True, blank=True)
    name=models.CharField(max_length=255, default=None, null=True, blank=True)
    status=models.CharField(max_length=255, default=None, null=True, blank=True)
    movie_unique=models.TextField(max_length=255, default=None, null=True, blank=True)
    poster=models.ImageField(upload_to="Posters",null=True, blank=True)
    description=models.TextField(max_length=255, default=None, null=True, blank=True)
    time=models.DecimalField(default=None,decimal_places=2, max_digits=20, blank=True, null=True)

class Slider(models.Model):
    content=models.ForeignKey("Content", null=True, blank=True)


class Watchers(models.Model):
    unique_code=models.CharField(max_length=255, default=None, null=True, blank=True) #from api online
    code_expiration=models.DateTimeField(default=None, null=True, blank=True)
    logged_in_counter=models.IntegerField(default=None, null=True, blank=True)
    last_login=models.DateTimeField(default=None, null=True, blank=True)
    devices=models.ForeignKey("Devices",null=True, blank=True,)
class Devices(models.Model):
    device1=models.CharField(max_length=255, default=None, null=True, blank=True)
    device2=models.CharField(max_length=255, default=None, null=True, blank=True)
