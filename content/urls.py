from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
url(r'^$', views.home,name="index"),
url(r'^index/$', views.IndexView.as_view()),
url(r'^mobflix/watch/(?P<pk>[0-9]+)/$', views.watch),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
