from django.conf.urls import patterns, include, url
from group4 import views
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'/adminIndex/$', views.adminIndex, name="adminIndex"),
    url(r'/adminShow/$', views.adminShow, name="adminShow"),
    url(r'/userShow/$', views.userShow, name="userShow"),
    url(r'/userShow/add/$', views.addNewPage, name="addNewPage"),
    url(r'/userShow/add/commit/$', views.commit, name="commit"),
    url(r'/adminIndex/view/(\w+)$', views.addpdf, name="addpdf"),
)