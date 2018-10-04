from .models import *
import django_filters


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = ['id','name','status','movie_unique','description','time']
