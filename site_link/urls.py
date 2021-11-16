from django.urls import path

from . import views
app_name = 'site_link'
urlpatterns = [
    path('',views.index, name='index'),
    path('CEM/', views.CEM, name='CEM'),
    path('public/',views.public, name='public'),
    path('gov/',views.gov, name='gov'),
    path('insitute/',views.insitute, name='insitute'),
    path('oversea/',views.oversea, name='oversea'),
    path('other/',views.other, name='other'),
    path('write/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
