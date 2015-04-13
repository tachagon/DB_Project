from django.conf.urls import patterns, include, url
from group3 import views

urlpatterns = patterns('',
    url(r'^prof2lang/$', views.prof2lang_index, name='prof2lang_index'),
)
