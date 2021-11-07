from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect


app_name = 'professor_hyun_8'
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.create, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('/great', views.index_2, name='index_2'),
    path('write/great', views.create_2, name='write_2'),
    path('<int:pk>/great', views.detail_2, name='detail_2'),
    path('<int:pk>/edit/great', views.update_2, name='update_2'),
    path('<int:pk>/delete/great', views.delete_2, name='delete_2'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)