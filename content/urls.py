from django.conf.urls import url,include
from django.contrib import admin
from . import views
from staff.views import UploadContent


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
url(r'^$', views.home,name="index"),
path('index/', views.IndexView.as_view()),
path('mobflix/watch/<int:id>/', views.watch),

#search for path

#retrieve all movies
path('content/all/', UploadContent.as_view()),

#retrieve a movie
path('content/item/<int:id>/', UploadContent.as_view()),

#retrieve  a movie category
path('content/item/<category>/',views.ContentSearchCategory.as_view()),
#verify token
path('content/item/verify/',views.VerifyVoucher.as_view())





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
