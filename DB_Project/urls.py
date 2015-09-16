from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views
from group1 import views
admin.autodiscover()
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DB_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('login.urls', namespace="login")),
    url(r'^group1', include('group1.urls', namespace="group1")),
    url(r'^group2', include('group2.urls', namespace="group2")),
    url(r'^group3', include('group3.urls', namespace="group3")),
    url(r'^group4', include('group4.urls', namespace="group4")),
    url(r'^group5', include('group5.urls', namespace="group5")),
    url(r'^group6', include('group6.urls', namespace="group6")),
    url(r'^group7', include('group7.urls', namespace="group7")),
    url(r'^site_media/(?P<path>.*)$',
       'django.views.static.serve',
      {'document_root' : BASE_DIR + '/media'})
)
