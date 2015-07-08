from django.conf.urls import patterns, include, url
from group2 import views

urlpatterns = patterns('',
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dataStudent/$', views.data_student, name='data_student'),
    url(r'^dataStudentEdit/$', views.data_student_edit, name='data_student_edit'),
    url(r'^getdataStudentEdit/$', views.get_data_student_edit, name='get_data_student_edit'),
    url(r'^search_student/$', views.search_student, name='search_student'),
    url(r'^search_student/profile/(\d+)/$', views.profile_admin, name='profile_admin'),
    url(r'^search_student/data_student/(\d+)/$', views.data_student_admin, name='data_student_admin'),
    url(r'^search_student/regis_result/(\d+)/$', views.regis_result_admin, name='regis_result_admin'),
    url(r'^search_student/viyanipon/(\d+)/$', views.viyanipon_admin, name='viyanipon_admin'),
    url(r'^viyanipon/$', views.viyanipon, name='viyanipon'),
    url(r'^viyaniponShow/$', views.viyaniponshow, name='viyaniponshow'),
    url(r'^registeration/$', views.registeration, name='registeration'),
    url(r'^regisResult/$', views.regis_result, name='regis_result'),
    url(r'^schoolRecord/$', views.school_record, name='school_record'),
    url(r'^school_record_admin/(\d+)/$', views.school_record_admin, name='school_record_admin'),
    url(r'^school_record_admin/$', views.school_record_admin_edit, name='school_record_admin_edit'),
    url(r'^search_course/$', views.search_course, name='search_course'),
    url(r'^Find_course/$', views.Find_course, name='Find_course'),
    url(r'^Put_Grade/$', views.Put_Grade, name='Put_Grade'),
)
