from django.conf.urls import patterns, include, url
from group4 import views
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'/userPage/$', views.userPage, name="userPage"),
    url(r'/userPage/commit/$', views.commitWithdrawCure, name="commitWithdrawCure"),
    url(r'/adminIndexPage/$', views.adminIndexPage, name="adminIndexPage"),
    url(r'/adminPage/commit_data/(\d+)$', views.commit_data, name="commit_data"),
    url(r'/userPage/addpdf/(\w+)$', views.addpdf, name="addpdf"),


    #url(r'/adminShow/$', views.adminShow, name="adminShow"),
)