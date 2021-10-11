from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect


app_name = 'seminar'
urlpatterns = [
    path('', views.AllListView.as_view(), name='index'),
    path('write/', views.create, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.notice_edit_view, name='notice_edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('download/<int:pk>/', views.download, name="download"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)