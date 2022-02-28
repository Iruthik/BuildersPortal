from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
path('',views.index,name='index'),
path('register',views.register,name ='register'),
# path('home',views.home,name ='home'),
path('login',views.login,name='login'),
path('alllogin',views.alllogin,name='alllogin'),
path('register/logout',views.logout,name ='logout'),
path('register/login',views.login,name='login'),
path('supplierlogin',views.supplierlogin,name='supplierlogin'),
path('customerlogin',views.customerlogin,name='customerlogin'),
path('register/workerupdate',views.workerupdate,name ='workerupdate'),
path('register/supplierupdate',views.supplierupdate,name='supplierupdate'),
path('register/customerupdate',views.customerupdate,name='customerupdate'),
path('register/home',views.home,name='home'),
path('supplierhome',views.supplierhome,name='supplierhome'),
path('customerhome',views.customerhome,name='customerhome'),
path('register/workerprofile',views.workerprofile,name='workerprofile'),
path('register/supplierprofile',views.supplierprofile,name='supplierprofile'),
path('register/customerprofile',views.customerprofile,name='customerprofile'),
path('supplierdetail/<int:worker_id>/',views.detail,name='detail'),
path('register/home/<int:supplier_id>/',views.detailsupplier,name='detailsupplier'),
path('register/search',views.searchdisplay,name='searchdisplay'),
path('post',views.post,name='post'),
path('supplierpost',views.supplierpost,name='supplierpost'),
]