from django.conf.urls import patterns, include, url
from group3 import views

urlpatterns = patterns('',
    url(r'^prof2lang/$', views.prof2lang_index, name='prof2lang_index'),
    url(r'^prof2lang/(\d+)/$', views.prof2lang_view, name='prof2lang_view'),
    url(r'^prof2lang/add/$', views.prof2lang_add, name='prof2lang_add'),
)
