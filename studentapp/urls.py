from django.urls import path

from studentapp import views

urlpatterns =[
    path('', views.log_fun, name='log'),
    path('logdata', views.logdata_fun),
    path('reg',views.reg_fun, name='reg'),#it will redirect to rigister.html page
    path('regdata', views.regdata_fun),  #it will create superuser account
    path('home', views.home_fun, name='home'),
    path('add_students', views.add_fun, name='add'),
    path('readdata', views.read_fun),     #returns record into student table
    path('display', views.display_fun, name='display'),  #display student table data in display.html
    path('update/<int:id>', views.update_fun, name='update'),
    path('delete/<int:id>', views.delete_fun, name='delete'),
    path('log_out', views.log_out_fun, name='log_out')
]