# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_url=models.FileField(upload_to="uploads",null=True, blank=True)
    name=models.CharField(max_length=255, default=None, null=True, blank=True)
    status=models.CharField(max_length=255, default=None, null=True, blank=True)
    movie_unique=models.TextField(max_length=255, default=None, null=True, blank=True)
    poster=models.ImageField(upload_to="Posters",null=True, blank=True)
    description=models.TextField(max_length=255, default=None, null=True, blank=True)
    time=models.DecimalField(default=None,decimal_places=2, max_digits=20, blank=True, null=True)
    category=models.ForeignKey("ContentCategory", null=True, blank=True,on_delete=models.CASCADE)
    genre=models.CharField(max_length=255, default=None, null=True, blank=True)
    stars=models.CharField(max_length=255, default=None, null=True, blank=True)
    director=models.CharField(max_length=255, default=None, null=True, blank=True)
    county = models.CharField(max_length=255, default=None, null=True, blank=True)
    video_qualify = models.CharField(max_length=255, default=None, null=True, blank=True)
    imdb = models.CharField(max_length=255, default=None, null=True, blank=True)
    release = models.CharField(max_length=255, default=None, null=True, blank=True)
    rating = models.CharField(max_length=255, default=None, null=True, blank=True)
    def __str__(self):
        return self.name
class ContentCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    def __str__(self):
        return self.name

class Slider(models.Model):
    content=models.ForeignKey("Content", null=True, blank=True,on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Watchers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_code=models.CharField(max_length=255, default=None, null=True, blank=True) #from api online
    code_expiration=models.DateTimeField(default=None, null=True, blank=True)
    logged_in_counter=models.IntegerField(default=None, null=True, blank=True)
    last_login=models.DateTimeField(default=None, null=True, blank=True)
    devices=models.ForeignKey("Devices",null=True, blank=True,on_delete=models.CASCADE)
class Devices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device1=models.CharField(max_length=255, default=None, null=True, blank=True)
    device2=models.CharField(max_length=255, default=None, null=True, blank=True)
