from django.conf.urls import patterns, include, url
from group6 import views

urlpatterns = patterns('',
    url(r'^Project_Docs/$', views.index, name='project_docs_index'),
    url(r'^Project_Docs/create_3forms/$', views.create_3forms, name='project_docs_create_3forms'),
    url(r'^Project_Docs/create_3forms/add$', views.create_3forms_add, name='project_docs_create_3forms_add'),
    url(r'^Project_Docs/view_approveProject/(\d+)/$', views.approveProject, name='project_docs_approveProject'),
    url(r'^Project_Docs/view_offerProject/(\d+)/$', views.offerProject, name='project_docs_offerProject'),
    url(r'^Project_Docs/view_researchProject/(\d+)/$', views.researchProject, name='project_docs_researchProject'),
    url(r'^Project_Docs/delete/(\d+)/$', views.deleteForm, name='project_docs_delete'),
    #url(r'^testpdf/(\d+)/$', views.genpdf, name='genpdf'),
)
