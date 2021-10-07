from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'paper_patent'
urlpatterns = [
    path('', views.index, name='index'),
    path('kor_jounal/', views.kor_jounal, name='kor_jounal'),
    path('world_conference/', views.world_conference, name='world_conference'),
    path('kor_conference/', views.kor_conference, name='kor_conference'),
    path('kor_thesis/', views.kor_thesis, name='kor_thesis'),
    path('world_thesis/', views.world_thesis, name='world_thesis'),
    path('property_1/', views.property_1, name='property_1'),
    path('property_2/', views.property_2, name='property_2'),
    path('property_3/', views.property_3, name='property_3'),
]