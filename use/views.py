from multiprocessing import context
from urllib import request
from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Worker,Supplier

from django.contrib.auth.models import User,auth

def index(request):
    return render(request,'use/index.html')

def register(request):
    if request.method == 'POST':
         username = request.POST['username']
         email = request.POST['email']
         password1 = request.POST['password1']
         password2 = request.POST['password2']
         role = request.POST['role']
         

         if password1 == password2 and role == "1" :
             if User.objects.filter(username =username).exists():
                 messages.info(request,'Username already exist...')
                 return redirect('register')

             elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email already exist...')
                 return redirect('register')

                    
             else:
                 user = User.objects.create_user(username=username,password=password1,email=email)
                 user.save()
                 print(role)
                 messages.info(request,'user created...')
                 return redirect('workerupdate')
       
                    
         elif password1 == password2 and role =="2": 
             if User.objects.filter(username =username).exists():
                 messages.info(request,'Username already exist...')
                 return redirect('register')

             elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email already exist...')
                 return redirect('register')

                    
             else:
                 user = User.objects.create_user(username=username,password=password1,email=email)
                 user.save()
                 print(role)
                 messages.info(request,'user created...')
                 return redirect('supplierupdate')
             
             
         elif password1 == password2 and role =="3":
               if User.objects.filter(username =username).exists():
                 messages.info(request,'Username already exist...')
                 return redirect('register')

               elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email already exist...')
                 return redirect('register')

                    
               else:
                 user = User.objects.create_user(username=username,password=password1,email=email)
                 user.save()
                 print(role)
                 messages.info(request,'user created...')
                 return redirect('customerupdate')
         else:
             messages.info(request,'password not matching!...')
             return redirect('register')

        
        
         


    else:
         return render(request,'use/register.html')   

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')    

    return render(request,'use/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')   


def home(request):
   
    return render(request,'use/home.html')


def workerupdate(request):
    return render(request,'use/worker_update.html')

def supplierupdate(request):
    return render(request,'use/supplier_update.html')    

def customerupdate(request):
    return render(request,'use/customer_update.html')

def workerprofile(request):
     if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        phone = request.POST['phone']
        description=request.POST['description']
        rate =request.POST['rate']
        location=request.POST['location']
        category = request.POST['category']
        availability=request.POST['availability']

        print(firstname)
        print(lastname)
        print(category)
        print(availability)


        context= {'firstname':firstname,
                   'lastname':lastname,
                   'phone':phone,
                   'description':description,
                   'rate':rate,
                   'location':location,
                   'category':category,
                   'availability':availability
        }
        

        worker= Worker(firstname=firstname,lastname=lastname,phone=phone,description=description,rate=rate,location=location,category=category,availability=availability)
        worker.save()
        print("worker profile created")
     return render(request,'use/profile.html',context)


def supplierprofile(request):

     if request.method == 'POST':
        shopname = request.POST['shopname']
        vendorname  = request.POST['vendorname']
        phone = request.POST['phone']
        description=request.POST['description']
        rate =request.POST['rate']
        location=request.POST['location']
        category = request.POST['category']
        availability=request.POST['availability']

        print(shopname)
        print(vendorname)
        print(category)
        print(availability)

        context= {'shopname':shopname,
                   'vendorname':vendorname,
                   'phone':phone,
                   'description':description,
                   'rate':rate,
                   'location':location,
                   'category':category,
                   'availability':availability
        }

        supplier = Supplier(shopname=shopname,vendorname=vendorname,phone=phone,description=description,rate=rate,location=location,category=category,availability=availability)
        supplier.save()
        print("Supplier profile created")

     return render(request,'use/profile_supplier.html',context)