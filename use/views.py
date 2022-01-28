from django import forms
import django
from django.shortcuts import redirect, render
from .models import userregister
from .forms import RegisterForm 
from django.contrib.auth.models import User,auth

def index(request):
    return render(request,'use/index.html')

def register(request):
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         user = User.objects.create_user(username=username,password=password1,email=email)
         user.save()
         print('user created')
         return redirect('/')
    
    else:
         return render(request,'use/register.html')   


