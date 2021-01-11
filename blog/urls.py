from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^about/kor/$', views.aboutkor_page, name='aboutkor_page'),
    url(r'^research/$', views.research_page, name='research_page'),
    url(r'^member/$', views.member_page, name='member_page'),
    url(r'^member/senior/$', views.member_senior, name='member_senior'),
    url(r'^member/research/$', views.member_res, name='member_res'),
    url(r'^notice/$', views.notice_page, name='notice_page'),
    url(r'^notice/(?P<id>[0-9]+)/$', views.notice_each, name='notice_each'),
    url(r'^contact/$', views.contact_page, name='contact_page'),

]
