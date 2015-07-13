from django.conf.urls import patterns, include, url
from group6 import views

urlpatterns = patterns('',
    url(r'^Project_Docs/$', views.index, name='project_docs_index'), #url of group6 app index page
    url(r'^Project_Docs/create_3forms/$', views.create_3forms, name='project_docs_create_3forms'), #url of create project forms page
    url(r'^Project_Docs/create_3forms/add$', views.create_3forms_add, name='project_docs_create_3forms_add'), #url for save data from project_docs_create_3forms to database
    url(r'^Project_Docs/view_approveProject/(\d+)/$', views.approveProject, name='project_docs_approveProject'), #url to view approveProject forms by project id
    url(r'^Project_Docs/view_offerProject/(\d+)/$', views.offerProject, name='project_docs_offerProject'), #url to view offerProject forms by project id
    url(r'^Project_Docs/view_researchProject/(\d+)/$', views.researchProject, name='project_docs_researchProject'), #url to view researchProject forms by project id
    url(r'^Project_Docs/view_timeLineProject/(\d+)/$', views.timeLineProject, name='project_docs_timeLineProject'), #url to view timeLineProject forms by project id
    url(r'^Project_Docs/view_approveProject/(\d+)/print/$', views.approveProjectPrint, name='project_docs_approveProject_print'), #url to print approveProject forms by project id
    url(r'^Project_Docs/view_offerProject/(\d+)/print/$', views.offerProjectPrint, name='project_docs_offerProject_print'), #url to view print offerProject forms by project id
    url(r'^Project_Docs/view_researchProject/(\d+)/print/$', views.researchProjectPrint, name='project_docs_researchProject_print'), #url to view print researchProject forms by project id
    url(r'^Project_Docs/view_timeLineProject/(\d+)/print/$', views.timeLineProjectPrint, name='project_docs_timeLineProject_print'), #url to view print timeLineProject forms by project id (black tab)
    url(r'^Project_Docs/view_timeLineProject/(\d+)/print_check/$', views.timeLineProjectPrintCheck, name='project_docs_timeLineProject_print_check'), #url to print timeLineProject forms by project id (checkbox)
    url(r'^Project_Docs/delete/(\d+)/$', views.deleteForm, name='project_docs_delete'), #url for delete project and all data of this project
    url(r'^Project_Docs/edit/(\d+)/$', views.edit_3forms, name='project_docs_edit'), #url for render edit project forms page by project id
    url(r'^Project_Docs/edit/(\d+)/update$', views.edit_3forms_update, name='project_docs_edit_update'), #url to update project forms data in database from project_docs_edit by project id
    url(r'^Project_Docs/add_categories_tester/(\d+)/$', views.add_categories_tester, name='project_docs_add_categories_tester'), #url for render page to set categories project number and tester
    url(r'^Project_Docs/add_categories_tester/(\d+)/add$', views.add_categories_tester_add, name='project_docs_add_categories_tester_add'), #url for save data from project_docs_add_categories_tester to database
    url(r'^Project_Docs/edit_categories_tester/(\d+)/$', views.edit_categories_tester, name='project_docs_edit_categories_tester'), #url for render edit categories project number and tester page by CategoriesProject id
    url(r'^Project_Docs/edit_categories_tester/(\d+)/update$', views.edit_categories_tester_update, name='project_docs_edit_categories_tester_update'), #url to update categories project number and tester data in database from project_docs_edit_categories_tester by CategoriesProject id
    url(r'^Project_Docs/add_notification/(\d+)/$', views.add_notification, name='project_docs_add_notification'), #url for render page to create new notification page
    url(r'^Project_Docs/add_notification/(\d+)/add$', views.add_notification_add, name='project_docs_add_notification_add'), #url for save data from project_docs_add_notification to database
    url(r'^Project_Docs/view_notification/(\d+)/$', views.view_notification, name='project_docs_view_notification'), #url for render page to view notification by notification id
    url(r'^Project_Docs/view_notification/(\d+)/reply_message/$', views.reply_message, name='project_docs_reply_message'), #url for render page to reply message on notification page
    url(r'^Project_Docs/view_notification/(\d+)/reply_message/add$', views.reply_message_add, name='project_docs_reply_message_add'), #url for save data from project_docs_reply_message to database
    url(r'^Project_Docs/view_notification/(?P<nID>\d+)/edit_message/(?P<mID>\d+)/$', views.edit_notification_message, name='project_docs_edit_notification_message'), #url for render page to edit message by message id
    url(r'^Project_Docs/view_notification/(?P<nID>\d+)/edit_message/(?P<mID>\d+)/update$', views.edit_notification_message_update, name='project_docs_edit_notification_message_update'), #url to update message data in database from project_docs_edit_notification_message by message id
    url(r'^Project_Docs/view_notification/(\d+)/delete$', views.delete_notification, name='project_docs_delete_notification'), #url for delete notification and all message of notification by notification id
)
