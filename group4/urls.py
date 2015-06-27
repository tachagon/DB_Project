from django.conf.urls import patterns, include, url
from group4 import views

urlpatterns = patterns('',
    url(r'/adminShow/$', views.adminShow, name="adminShow"),
)
