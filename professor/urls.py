from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'professor'
urlpatterns = [
    path('', views.index, name='index'),
    path('professor_Hyun/', views.professor_Hyun, name='professor_Hyun'),
    path('professor_Lee/', views.professor_Lee, name='professor_Lee'),
]