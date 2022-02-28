from multiprocessing import context
from pickle import READONLY_BUFFER
from urllib import request
from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Worker,Supplier,Customer,Workers

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
def alllogin(request):
    return render(request,'use/alllogin.html')         

def login(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')    

    return render(request,'use/login.html')
def supplierlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('supplierhome')
        else:
            messages.info(request,'invalid credentials')
            return redirect('supplierlogin')    

    return render(request,'use/supplierlogin.html')
def customerlogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('customerhome')
        else:
            messages.info(request,'invalid credentials')
            return redirect('customerlogin')    

    return render(request,'use/customerlogin.html')
def logout(request):
    auth.logout(request)
    return redirect('index')   


def home(request):
    worker_list = Worker.objects.all()
    context={
        'worker_list':worker_list
    }
    # print(worker_list)
    return render(request,'use/home.html',context)
def supplierhome(request):
     supplier_list = Supplier.objects.all()
     context={
        'supplier_list':supplier_list
        }
     return render(request,'use/supplierhome.html',context)
def customerhome(request):
    worker_list = Worker.objects.all()
    supplier_list = Supplier.objects.all()
    context={
        'worker_list':worker_list,
        'supplier_list':supplier_list
        }
    # print(worker_list)
    return render(request,'use/customerhome.html',context)
     

def workerupdate(request):
    return render(request,'use/worker_update.html')

def supplierupdate(request):
    
    return render(request,'use/supplier_update.html')    

def customerupdate(request):
    
    return render(request,'use/customer_update.html')

def workerprofile(request):
 
 
     if request.method == 'POST':
        worker= Worker()
        worker.firstname = request.POST['firstname']
        worker.lastname  = request.POST['lastname']
        worker.phone = request.POST['phone']
        worker.description=request.POST['description']
        worker.rate =request.POST['rate']
        worker.location=request.POST['location']
        worker.category = request.POST['category']
        worker.availability=request.POST['availability']
        # worker.user = 
        
        if len(request.FILES) != 0:
              worker.image = request.FILES['image']


       
        worker.save()
        # messages.success(request,'WorkerProfile Updated')
        # print(worker.image)
     return render(request,'use/login.html')


def supplierprofile(request):

     if request.method == 'POST':
        supplier =Supplier() 
        supplier.shopname = request.POST['shopname']
        supplier.vendorname  = request.POST['vendorname']
        supplier.phone = request.POST['phone']
        supplier.description=request.POST['description']        
        supplier.location=request.POST['location']
        supplier.category = request.POST['category']
        supplier.availability=request.POST['availability']

        if len(request.FILES) != 0:
              supplier.image = request.FILES['image']


        
        
        supplier.save()
        
        print("Supplier profile created")

     return render(request,'use/supplierlogin.html',)

def customerprofile(request):
    
      if request.method == 'POST':
        customer =Customer() 
        customer.firstname = request.POST['firstname']
        customer.lastname  = request.POST['lastname']
        customer.phone = request.POST['phone']     
        customer.location=request.POST['location']
      
         
        if len(request.FILES) != 0:
              customer.image = request.FILES['image']

        customer.save()
        print("Customer profile created")

      return render(request,'use/customerlogin.html')     

def detail(request,worker_id):
    worker = Worker.objects.get(pk=worker_id)
  
    context={
        'worker':worker,
    }
    return render(request,'use/worker_detail.html',context)
def detailsupplier(request,supplier_id):
    supplier = Supplier.objects.get(pk=supplier_id)   
    context ={
        'supplier':supplier
    }
    print(context)
    return render(request,'use/supplier_detail.html',context) 

def searchdisplay(request):
    context={}
    if request.method == 'POST':
        word =  request.POST['word']
        role = request.POST['role']
        
        if  word == "":
            return redirect(request,'home')
        else:  
            if role == "1": 
           
               searchwr= Worker.objects.filter(location__contains=word).all()
              
               context={
                     'searchwr': searchwr
                 }
            elif role == "2": 
               print(role)
               searchsl= Supplier.objects.filter(location__contains=word).all()
               print(searchsl)
               context={
                     'searchsl': searchsl
                 }
               return render(request,'use/workersearch.html',context)       
      
            elif role =="3": 
               searchc=Customer.objects.filter(location__contains=word).all()
                  
               context= {
                     'searchc': searchc
                 }   
               return render(request,'use/workersearch.html',context)
           
    return render(request,'use/workersearch.html',context)

def post(request):
    return render(request,'use/post.html')
def supplierpost(request):
    return render(request,'use/supplierpost.html')    
def addproduct(request):
    return render(request,'use/addproduct.html')    