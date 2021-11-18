from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'research_pj'
urlpatterns = [
    path('', views.index, name='index'),
    path('PM/', views.PM, name='PM'),
    path('VE/', views.VE, name='VE'),
    path('Clame/', views.Clame, name='Clame'),
    path('PMIS/', views.PMIS, name='PMIS'),
    path('EVMS/', views.EVMS, name='EVMS'),
    path('Sustain/', views.Sustain, name='Sustain'),
    path('RISK/', views.RISK, name='RISK'),
    path('QC/', views.QC, name='QC'),
    path('DigitalTwin/',views.DigitalTwin, name='DigitalTwin'),
    path('AR/',views.AR, name='AR'),
]