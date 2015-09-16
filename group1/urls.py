from django.conf.urls import patterns, include, url
from group1 import views

urlpatterns = patterns('',
    url(r'/index/$', views.index, name='index'),
    url(r'/search_file/$', views.search_file, name='search_file'),
    url(r'/send_email/(?P<doc_id>\d+)/$', views.send_email, name='send_email'),
    url(r'/sender/$', views.sender, name='sender'),
    url(r'/add_person/$', views.sender, name='add_person'),
    url(r'/upload_file/$', views.upload_file, name='upload_file'),
    url(r'/edit_file/(?P<doc_id>\d+)/$', views.edit_file, name='edit_file'),
    url(r'/edit_this_file/$', views.edit_this_file, name='edit_this_file'),
    url(r'/add_category/$', views.add_category, name='add_category'),
    url(r'/add_people/$', views.add_people, name='add_people'),
	
)
