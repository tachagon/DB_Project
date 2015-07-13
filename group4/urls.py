from django.conf.urls import patterns, include, url
from group4 import views
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'/userPage/$', views.userPage, name="userPage"),
    url(r'/userPage/commitWC/$', views.commitWithdrawCure, name="commitWithdrawCure"),
    url(r'/userPage/commitWS/$', views.commitWithdrawStudy, name="commitWithdrawStudy"),
    url(r'/adminIndexPage/$', views.adminIndexPage, name="adminIndexPage"),
    url(r'/adminPage/commit_data/(\d+)$', views.commit_data, name="commit_data"),
    url(r'/userPage/addpdf/(\w+)$', views.addpdf, name="addpdf"),
    url(r'/userPage/addpdf2/(\w+)$', views.addpdf2, name="addpdf2"),
    url(r'/userPage/add/commitf/$', views.commitf, name="commitf"),
    url(r'/userPage/add/commitm/$', views.commitm, name="commitm"),
    url(r'/userPage/add/commits/$', views.commits, name="commits"),
    url(r'/userPage/add/commitc/$', views.commitc, name="commitc"),
    url(r'/userPage/add/commitac/(\d+)$', views.commitac, name="commitac"),
    url(r'/userPage/add/commitf2/(\d+)$', views.commitf2, name="commitf2"),
    url(r'/userPage/add/commitm2/(\d+)$', views.commitm2, name="commitm2"),
    url(r'/userPage/add/commits2/(\d+)$', views.commits2, name="commits2"),
    url(r'/userPage/add/commitc2/(\d+)$', views.commitc2, name="commitc2"),


    #url(r'/adminShow/$', views.adminShow, name="adminShow"),
)