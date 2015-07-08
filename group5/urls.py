from django.conf.urls import patterns, include, url
from group5 import views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/status/$', views.table_user.as_view() , name = 'status'  ),
    #url(r'^/status/$', views.exampleCurrentUser , name = 'status'  ),
    url(r'^/status/$', views.table_status , name = 'status'  ),
    url(r'^/company/$', views.table_company , name = 'company'  ),
    #url(r'^/form1/$', views.tablef1_status , name = 'form1'  ),
    url(r'^/addpet/$', views.table_addpet , name = 'addpet'  ),
    url(r'^/form4/$', views.tablef4_status , name = 'form4'  ),
    #vvvvvvvvvvvvvvvvvvvvvv      Add            vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    url(r'^/pdf/$', views.table_pdf , name = 'pdf'  ),
    url(r'^/form2/$', views.table_waitPettition , name = 'form2'  ),
    url(r'^/form3/$', views.table_Finish , name = 'form3'  ),
    url(r'^/form5/$', views.table5_waitPettition , name = 'form5'  ),
    url(r'^/delete/(\d+)/$', views.deleteForm, name='status_delete'),
    url(r'^/status/print/(\d+)$', views.printForm, name='status_print'),
    url(r'^/status/edit/(\d+)$', views.editForm, name='status_edit'),
    #vvvvvvvvvvvvvvvv       new  vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    url(r'^/main/$', views.main_dep , name = 'main'  ),
    url(r'^/main2/$', views.main_dep2 , name = 'main2'  ),
    url(r'^/student1/$', views.main_dep3 , name = 'student1'  ),
    #-----------------------------------------new aom ------------------------------------------
    url(r'^/mainG5/$', views.table_mainG5 , name = 'mainG5'  ),
    url(r'^/status1/$', views.table_status1 , name = 'status1'  ),
    url(r'^/upload/$',views.upload,name = 'upload'),
    url(r'^/search/$',views.search,name = 'search'),
    url(r'^/ChangeStatus/$',views.table_ChangeStatus,name = 'change1'),
    url(r'^/ChangeStatus2/$',views.table_ChangeStatus2,name = 'change2'),
    url(r'^/edit/$' , views.edit,name="edit"),
    
    url(r'^/form1/$',views.form1,name = 'form1'),
    url(r'^/accept_trainee_print/$',views.accept_trainee_print,name = 'accept_trainee_print'),
    
    url(r'^/form2_p/$',views.form2,name = 'form2_p'),
    url(r'^/reporting/$',views.reporting,name = 'reporting'),
)
