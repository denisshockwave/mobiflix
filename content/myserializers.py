from .models import *
from rest_framework import serializers

class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCategory
        fields=('name','id')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('number','id')


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('number', 'id')

class ContentSerializer(serializers.ModelSerializer):
    category=ContentCategorySerializer()
    episode = EpisodeSerializer()
    season = SeriesSerializer()
    class Meta:
        model=Content
        fields=('id','name','status','category','movie_unique','video_url','poster',
        'description','time','genre','stars','director','county',
        'video_qualify','imdb','release','rating','season_available','season','episode','slug','trailer_url')

class ContentDisplaySerializer(serializers.ModelSerializer):
    category =ContentCategorySerializer()
    episode = EpisodeSerializer()
    season = SeriesSerializer()
    class Meta:
        model=Content
        fields = ('id', 'name', 'status', 'category', 'movie_unique', 'poster', 'description', 'time', 'genre',
                  'stars', 'director', 'county', 'video_qualify', 'imdb', 'release', 'rating', 'season', 'episode', 'slug','trailer_url',)



