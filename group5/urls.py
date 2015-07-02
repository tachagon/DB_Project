from django.conf.urls import patterns, include, url
from group5 import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/status/$', views.status, name='status'),
    url(r'^/company/$', views.company, name='company'),
    url(r'^/department_new/$', views.department_new, name='department_new'),
)
