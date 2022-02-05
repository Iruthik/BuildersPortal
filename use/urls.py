from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('register',views.register,name ='register'),
path('home',views.home,name ='home'),
path('login',views.login,name='login'),
path('logout',views.logout,name ='logout'),
path('register/workerupdate',views.workerupdate,name ='workerupdate'),
path('register/supplierupdate',views.supplierupdate,name='supplierupdate'),
path('register/customerupdate',views.customerupdate,name='customerupdate'),
path('register/home',views.home,name='home'),
]