from .models import *
from rest_framework import serializers

class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields=('name',)

class ContentSerializer(serializers.ModelSerializer):
    category=ContentCategorySerializer()
    class Meta:
        model=Content
        fields=('id','name','status','category','movie_unique','video_url','poster','description','time','genre','stars','director','county','video_qualify','imdb','release','rating')

class ContentDisplaySerializer(serializers.ModelSerializer):
    category =ContentCategorySerializer()
    class Meta:
        model=Content
        fields=('id','name','status','category','movie_unique','poster','description','time','genre','stars','director','county','video_qualify','imdb','release','rating')
