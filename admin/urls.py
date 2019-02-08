from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
#list a movie..upload
path('admin/content/upload',UploadContent.as_view())
path('admin/content/delete/<int:id>/', views.UploadContentDetailView.as_view()),
path('admin/content/update/<int:id>/', views.UploadContentDetailView.as_view()),

path('admin/category/list/',ContentCategory.as_view())
path('admin/category/item/',ContentCategoryDetail.as_view())
p
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
