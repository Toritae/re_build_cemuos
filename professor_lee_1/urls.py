from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect


app_name = 'professor_lee_1'
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.create, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('/thesis', views.index_2, name='index_2'),
    path('write/thesis', views.create_2, name='write_2'),
    path('<int:pk>/thesis', views.detail_2, name='detail_2'),
    path('<int:pk>/edit/thesis', views.update_2, name='update_2'),
    path('<int:pk>/delete/thesis', views.delete_2, name='delete_2'),
    path('/academic', views.index_3, name='index_3'),
    path('write/academic', views.create_3, name='write_3'),
    path('<int:pk>/academic', views.detail_3, name='detail_3'),
    path('<int:pk>/edit/academic', views.update_3, name='update_3'),
    path('<int:pk>/delete/academic', views.delete_3, name='delete_3'),
    path('/world_conf', views.index_4, name='index_4'),
    path('write/world_conf', views.create_4, name='write_4'),
    path('<int:pk>/world_conf', views.detail_4, name='detail_4'),
    path('<int:pk>/edit/world_conf', views.update_4, name='update_4'),
    path('<int:pk>/delete/world_conf', views.delete_4, name='delete_4'),
    path('/kor_conf', views.index_5, name='index_5'),
    path('write/kor_conf', views.create_5, name='write_5'),
    path('<int:pk>/kor_conf', views.detail_5, name='detail_5'),
    path('<int:pk>/edit/kor_conf', views.update_5, name='update_5'),
    path('<int:pk>/delete/kor_conf', views.delete_5, name='delete_5'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)