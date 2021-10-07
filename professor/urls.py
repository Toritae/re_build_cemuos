from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'professor'
urlpatterns = [
    path('', views.index, name='index'),
    path('professor_Hyun/', views.professor_Hyun, name='professor_Hyun'),
    path('professor_Hyun/1', views.professor_Hyun_1, name='professor_Hyun_1'),
    path('professor_Hyun/2', views.professor_Hyun_2, name='professor_Hyun_2'),
    path('professor_Hyun/3', views.professor_Hyun_3, name='professor_Hyun_3'),
    path('professor_Hyun/4', views.professor_Hyun_4, name='professor_Hyun_4'),
    path('professor_Hyun/5', views.professor_Hyun_5, name='professor_Hyun_5'),
    path('professor_Hyun/6', views.professor_Hyun_6, name='professor_Hyun_6'),
    path('professor_Hyun/7', views.professor_Hyun_7, name='professor_Hyun_7'),
    path('professor_Hyun/8', views.professor_Hyun_8, name='professor_Hyun_8'),
    
    path('professor_Lee/', views.professor_Lee, name='professor_Lee'),
    path('professor_Lee/1', views.professor_Lee_1, name='professor_Lee_1'),
    path('professor_Lee/6', views.professor_Lee_6, name='professor_Lee_6'),
    path('professor_Lee/7', views.professor_Lee_7, name='professor_Lee_7'),
    path('professor_Lee/8', views.professor_Lee_8, name='professor_Lee_8'),
]