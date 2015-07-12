#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from login import views, views_profile

urlpatterns = patterns('',
    # index, login, logout, menu and register --------------------------------------------------------------------------
    url(r'^$',                              views.index,                name='index'),
    url(r'^login/$',                        views.user_login,           name='login'),
    url(r'^logout/$',                       views.user_logout,          name='logout'),
    url(r'^menu/$',                         views.menu,                 name='menu'),
    url(r'^register/$',                     views.user_register,        name='register'),
    url(r'^test/$',                         views.testDateField,        name='testDateField'),
    # information user profile -----------------------------------------------------------------------------------------
    url(r'^profile/$',                      views_profile.index,        name='profile_index'),
    # edit user profile ------------------------------------------------------------------------------------------------
    url(r'^profile/edit/thainame/$',        views_profile.editThaiName, name='profile_editThaiName'),
    url(r'^profile/edit/engname/$',         views_profile.editEngName,  name='profile_editEngName'),
    url(r'^profile/edit/username/$',        views_profile.editUsername, name='profile_editUsername'),
    url(r'^profile/edit/email/$',           views_profile.editEmail,    name='profile_editEmail'),
    url(r'^profile/edit/tel/$',             views_profile.editTel,      name='profile_editTel'),
    url(r'^profile/edit/address/$',         views_profile.editAddress,  name='profile_editAddress'),
    url(r'^profile/edit/office/$',          views_profile.editOffice,   name='profile_editOffice'),
    url(r'^profile/edit/account/$',         views_profile.editAccount,  name='profile_editAccount'),
    url(r'^profile/edit/prefixname/$',      views_profile.editPrefixName,name='profile_editPrefixName'),
    # change password of user ------------------------------------------------------------------------------------------
    url(r'^profile/edit/password/$',        views_profile.editPassword, name='profile_editPassword'),
    # information student profile --------------------------------------------------------------------------------------
    url(r'^profile/student/$',              views_profile.student,      name='profile_student'),
    # information teacher profile --------------------------------------------------------------------------------------
    url(r'^profile/teacher/$',              views_profile.teacher,      name='profile_teacher'),
    # edit teacher profile ---------------------------------------------------------------------------------------------
    url(r'^profile/teacher/edit/prefix/$',  views_profile.editPrefix,   name='profile_editPrefix'),
    url(r'^profile/teacher/edit/shortname/$',views_profile.editShortname,name='profile_editShortname'),
    url(r'^profile/teacher/edit/position/$',views_profile.editTeacherPosition, name='profile_editTeacherPosition'),
)
