from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect


app_name = 'ref_board'

def protected_file(request, path, document_root=None):
    messages.error(request, "접근 불가")
    return redirect('/')

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.create, name='write'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.notice_edit_view, name='notice_edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('download/<int:pk>', views.download, name="download"),
]

urlpatterns += static(settings.MEDIA_URL, protected_file, document_root=settings.MEDIA_ROOT)