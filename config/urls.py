"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import views

urlpatterns = [
    path('site_link/',include('site_link.urls')),
    path('pj_board/',include('pj_board.urls')),
    path('pj_board_gov/',include('pj_board_gov.urls')),
    path('scem/',include('scem.urls')),
    path('paper_patent/',include('paper_patent.urls')),
    path('notice/',include('notice.urls')),
    path('free/',include('free.urls')),
    path('professor/',include('professor.urls')),
    path('research_pj/',include('reserch_pj.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('common/', include('common.urls')),
    path('member_board_MA/',include('member_board_MA.urls')),
    path('member_board_Phd/',include('member_board_Phd.urls')),
    path('member_board_alum_MA/',include('member_board_alum_MA.urls')),
    path('member_board_alum_Phd/',include('member_board_alum_Phd.urls')),
    path('member_board_alum_MA_city/',include('member_board_alum_MA_city.urls')),
    path('member_board_alum_special/',include('member_board_alum_special.urls')),
    # path('ref_room/',include('reference_board.urls')),
    # path('photo/',include('photo.urls')),
    # path('seminar/',include('seminar.urls')),
    # path('QA/',include('QA.urls')),
    path('ref_room/', include('reference_board.urls')),
    path('QA/', include('Q_A.urls')),
    path('seminar/', include('seminar.urls')),
    path('photo/', include('photo.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('',views.index, name='index'),
    path('kor_conference/', include('kor_conference.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
