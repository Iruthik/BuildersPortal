from django import forms
import django
from django.shortcuts import redirect, render
from django.contrib import messages
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

         if password1 == password2:
             if User.objects.filter(username =username).exists():
                 messages.info(request,'Username already exist...')
                 return redirect('register')

             elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email already exist...')
                 return redirect('register')

                    
             else:
                 user = User.objects.create_user(username=username,password=password1,email=email)
                 user.save()
                 messages.info(request,'user created...')
                 return redirect('/')

                    
             
         else:
             messages.info(request,'password not matching!...')
             return redirect('register')
         return redirect('/')
    
    else:
         return render(request,'use/register.html')   


