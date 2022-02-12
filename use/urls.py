from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('register',views.register,name ='register'),
# path('home',views.home,name ='home'),
path('login',views.login,name='login'),
path('register/logout',views.logout,name ='logout'),
path('register/login',views.login,name='login'),
path('register/workerupdate',views.workerupdate,name ='workerupdate'),
path('register/supplierupdate',views.supplierupdate,name='supplierupdate'),
path('register/customerupdate',views.customerupdate,name='customerupdate'),
path('register/home',views.home,name='home'),
path('register/workerprofile',views.workerprofile,name='workerprofile'),
path('register/supplierprofile',views.supplierprofile,name='supplierprofile'),
path('register/customerprofile',views.customerprofile,name='customerprofile'),
]