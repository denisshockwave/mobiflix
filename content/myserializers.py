from .models import *
from rest_framework import serializers

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields=('id','video_url','name','status','movie_unique','video_url','poster','description','time')
