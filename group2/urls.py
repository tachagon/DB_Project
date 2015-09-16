from django.conf.urls import patterns, include, url
from group2 import views

urlpatterns = patterns('',
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dataStudent/$', views.data_student, name='data_student'),
    url(r'^dataStudentEdit/$', views.data_student_edit, name='data_student_edit'),
    url(r'^getdataStudentEdit/$', views.get_data_student_edit, name='get_data_student_edit'),
    url(r'^search_student/$', views.search_student, name='search_student'),
    url(r'^search_student/profile/(\d+)/$', views.profile_admin, name='profile_admin'),
    url(r'^search_student/regis_result/(\d+)/$', views.regis_result_admin, name='regis_result_admin'),
    url(r'^search_student/viyanipon_admin/(\d+)/$', views.viyanipon_admin, name='viyanipon_admin'),
    url(r'^search_student/admin_look_school_record/(\d+)/$', views.admin_look_school_record, name='admin_look_school_record'),


    url(r'^admin_look_school_record/$', views.admin_look_school_record, name='admin_look_school_record'),
    url(r'^registeration/$', views.registeration, name='registeration'),
    url(r'^regisResult/$', views.regis_result, name='regis_result'),
    url(r'^schoolRecord/$', views.school_record, name='school_record'),
    url(r'^school_record_admin/(\d+)/$', views.school_record_admin, name='school_record_admin'),
    url(r'^school_record_admin/$', views.school_record_admin_edit, name='school_record_admin_edit'),
    url(r'^search_course/$', views.search_course, name='search_course'),
    url(r'^Find_course/$', views.Find_course, name='Find_course'),
    url(r'^Find_course_admin/$', views.Find_course_admin, name='Find_course_admin'),
    url(r'^Edit_course_admin/$', views.Edit_course_admin, name='Edit_course_admin'),                       

    url(r'^Admin_check_register/$', views.Admin_check_register, name='Admin_check_register'),
    url(r'^Add_course_admin/$', views.Add_course_admin, name='Add_course_admin'),
    url(r'^Admin_drop/$', views.Admin_drop, name='Admin_drop'),
    url(r'^drop/$', views.drop, name='drop'),
    url(r'^drop_admin/$', views.drop_admin, name='drop_admin'),
    url(r'^registeration_admin/$', views.registeration_admin, name='registeration_admin'),
    url(r'^find_registeration_admin/$', views.find_registeration_admin, name='find_registeration_admin'),                  
    url(r'^Find_Admin_check_register/$', views.Find_Admin_check_register, name='Find_Admin_check_register'),
    url(r'^Update_check_admin/$', views.Update_check_admin, name='Update_check_admin'),
    url(r'^Admin_check_drop/$', views.Admin_check_drop, name='Admin_check_drop'),
    url(r'^Find_Admin_check_drop/$', views.Find_Admin_check_drop, name='Find_Admin_check_drop'),
    url(r'^Find_course_drop/$', views.Find_course_drop, name='Find_course_drop'),
    url(r'^Update_check_drop/$', views.Update_check_drop, name='Update_check_drop'),
    url(r'^Find_school_record_admin/$', views.Find_school_record_admin, name='Find_school_record_admin'),
    url(r'^Edit_school_record_admin/$', views.Edit_school_record_admin, name='Edit_school_record_admin'),
    url(r'^Add_register/$', views.Add_register, name='Add_register'),  
    url(r'^viyanipon/$', views.viyanipon, name='viyanipon'),
    url(r'^edit_viyanipon/$', views.edit_viyanipon, name='edit_viyanipon'),
    url(r'^Add_edit_viyanipon/$', views.Add_edit_viyanipon, name='Add_edit_viyanipon'),
                  

      


                       
)


