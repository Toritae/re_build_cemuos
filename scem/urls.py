from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'scem'
urlpatterns = [
    path('', views.index, name='index'),
    path('way_to_come/', views.come, name='come'),
    path('lab_bylaws/', views.bylaws, name='bylaws'),
]