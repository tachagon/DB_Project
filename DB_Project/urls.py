from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views
from group1 import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DB_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('login.urls', namespace="login")),
    url(r'^group1', include('group1.urls', namespace="group1")),
)
