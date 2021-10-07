from django.urls import path

from . import views
app_name = 'site_link'
urlpatterns = [
    path('', views.index, name='index'),
    path('public/',views.public, name='public'),
    path('gov/',views.gov, name='gov'),
    path('insitute/',views.insitute, name='insitute'),
    path('oversea/',views.oversea, name='oversea'),
    path('other/',views.other, name='other'),
]
