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
    path('kor_jounal/', include('kor_jounal.urls')),
    path('kor_thesis/', include('kor_thesis.urls')),
    path('world_conference/', include('world_conference.urls')),
    path('world_jounal/', include('world_jounal.urls')),
    path('thesis_ma/', include('thesis_ma.urls')),
    path('property_1/', include('property_1.urls')),
    path('property_2/', include('property_2.urls')),
    path('property_3/', include('property_3.urls')),
    path('professor_hyun_1/', include('professor_hyun_1.urls')),
    path('professor_hyun_2/', include('professor_hyun_2.urls')),
    path('professor_hyun_3/', include('professor_hyun_3.urls')),
    path('professor_hyun_4/', include('professor_hyun_4.urls')),
    path('professor_hyun_5/', include('professor_hyun_5.urls')),
    path('professor_hyun_6/', include('professor_hyun_6.urls')),
    path('professor_hyun_7/', include('professor_hyun_7.urls')),
    path('professor_hyun_8/', include('professor_hyun_8.urls')),
    path('professor_lee_1/', include('professor_lee_1.urls')),
    path('professor_lee_2/', include('professor_lee_2.urls')),
    path('professor_lee_3/', include('professor_lee_3.urls')),
    path('professor_lee_4/', include('professor_lee_4.urls')),
    path('professor_lee_5/', include('professor_lee_5.urls')),
    path('professor_lee_6/', include('professor_lee_6.urls')),
    path('professor_lee_7/', include('professor_lee_7.urls')),
    path('professor_lee_8/', include('professor_lee_8.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
