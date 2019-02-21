from django.conf.urls import url,include
from django.contrib import admin
from . import views



from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token


urlpatterns = [
url(r'^$', views.home,name="index"),
path('index/', views.IndexView.as_view()),
path('mobflix/watch/<int:id>/', views.watch),

#search for path

#retrieve all movies
path('content/all/', views.UploadContent.as_view()),

#retrieve a movie
path('content/item/<id>/<voucher>/', views.UploadContentVerifyView.as_view()),

#retrieve  a movie category
path('content/category/<category>/',views.ContentSearchCategory.as_view()),
#verify token
path('content/item/verify/<voucher>/',views.VerifyVoucher.as_view()),

path('content/search/',views.SearchQuery.as_view()),
path('content/series/<slug>/', views.SeriesDetailView.as_view()),



path('admin/content/upload',views.UploadContent.as_view()),
path('admin/content/delete/<id>/', views.UploadContentDetailView.as_view()),
path('admin/content/update/<id>/', views.UploadContentDetailView.as_view()),


path('admin/category/list/',views.ContentCategoryView.as_view()),
path('admin/category/item/',views.ContentCategoryDetailView.as_view()),


#token
path('admin/v1/login/', obtain_jwt_token),
path('admin/v1/refresh/', refresh_jwt_token),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
