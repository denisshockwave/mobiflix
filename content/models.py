# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
import uuid
# Create your models here.

class Content(models.Model):
    CHOICES = (
        ('Y', 'YES'),
        ('N', 'NO'),
    )
 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_url=models.FileField(upload_to="uploads",null=True, blank=True)
    trailer_url = models.FileField(upload_to="trailer", null=True, blank=True)
    name=models.CharField(max_length=255, default=None, null=True, blank=True)
    slug = models.SlugField(
        max_length=1000, default="movie", null=True, blank=True)
    status = models.CharField(
        max_length=255, default=None, null=True, blank=True, choices=CHOICES)
    movie_unique=models.TextField(max_length=255, default=None, null=True, blank=True)
    poster=models.ImageField(upload_to="Posters",null=True, blank=True)
    description=models.TextField(max_length=255, default=None, null=True, blank=True)
    time=models.DecimalField(default=None,decimal_places=2, max_digits=20, blank=True, null=True)
    category=models.ForeignKey("ContentCategory", null=True, blank=True,on_delete=models.PROTECT)
    genre=models.CharField(max_length=255, default=None, null=True, blank=True)
    stars=models.CharField(max_length=255, default=None, null=True, blank=True)
    director=models.CharField(max_length=255, default=None, null=True, blank=True)
    county = models.CharField(max_length=255, default=None, null=True, blank=True)
    video_qualify = models.CharField(max_length=255, default=None, null=True, blank=True)
    imdb = models.CharField(max_length=255, default=None, null=True, blank=True)
    release = models.CharField(max_length=255, default=None, null=True, blank=True)
    rating = models.CharField(max_length=255, default=None, null=True, blank=True)
    season= models.ForeignKey("Series", null=True, blank=True, on_delete=models.PROTECT)
    episode = models.ForeignKey("Episode", null=True, blank=True, on_delete=models.PROTECT)
    season_available = models.CharField(
        max_length=255, default=None, null=True, blank=True,choices=CHOICES)
    time_uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.name:
            return self.name
        else:
            return '-----'


    def save(self, *args, **kwargs):
        if self.season_available == "Y":
            
            self.slug = slugify(self.name)+"-"+str(self.season.number)
        else:
            self.slug = slugify(self.name)

        
        super(Content, self).save(*args, **kwargs)

class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number= models.IntegerField( default=0, null=True, blank=True)

    def __str__(self):
        return str(self.number)


class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(
             default=0, null=True, blank=True)
    tagline = models.CharField(
        max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.number)
class ContentCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    def __str__(self):
        return self.name


class ErrorLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255, default=None, null=True, blank=True)

    message = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    time_logged= models.DateTimeField(auto_now_add=True)
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
    paid_count = models.IntegerField(default=0, null=True, blank=True)
    count = models.IntegerField(default=0, null=True, blank=True)


class Devices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device1=models.CharField(max_length=255, default=None, null=True, blank=True)
    device2=models.CharField(max_length=255, default=None, null=True, blank=True)
 

class MovieServer(models.Model):
    ip = models.CharField(max_length=255, default="http://127.0.0.1:8000", null=True, blank=True)

# class VoucherCounter(models.Model):
#     id = models.UUIDField(
#          primary_key=True, default=uuid.uuid4, editable=False)
#     paid_count = models.IntegerField(default=0, null=True, blank=True)
#     count= models.IntegerField(default=0, null=True, blank=True)
 
#     voucher =models.CharField(max_length=255, default=None, null=True, blank=True)
 
