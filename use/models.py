from datetime import datetime
import os
from django.db import models
from os.path import join
from django.contrib.auth.models import User

# Create your models here.

class Workers(models.Model):
      def __str__(self):
             return self.firstname
      def get_filename(instance,filename):
             old_name = filename
             current_time=datetime.now().strftime('%Y%m%d%H;%M:%S')
             filename="%s%s"%(current_time,old_name)
             return os.path.join('uploads/',filename)
     
     
   
      image = models.ImageField(upload_to=get_filename,null=True,blank=True)
      firstname = models.CharField(max_length=200)
      lastname  = models.CharField(max_length=200)
      phone     = models.CharField(max_length=200)
      description= models.CharField(max_length=2000)
      rate=models.FloatField()
      location=models.CharField(max_length=200)
      category=models.CharField(max_length=200)
      availability=models.CharField(max_length=200)



class Worker(models.Model):

        def __str__(self):
             return self.firstname
        def get_filename(instance,filename):
             old_name = filename
             current_time=datetime.now().strftime('%Y%m%d%H;%M:%S')
             filename="%s%s"%(current_time,old_name)
             return os.path.join('uploads/',filename)
     
      
        image = models.ImageField(upload_to=get_filename,null=True,blank=True)
        firstname = models.CharField(max_length=200)
        lastname  = models.CharField(max_length=200)
        phone     = models.CharField(max_length=200)
        description= models.CharField(max_length=2000)
        rate=models.FloatField()
        location=models.CharField(max_length=200)
        category=models.CharField(max_length=200)
        availability=models.CharField(max_length=200)

class Supplier(models.Model):

        
        def __str__(self):
             return self.shopname
        def get_filename(instance,filename):
             old_name = filename
             current_time=datetime.now().strftime('%Y%m%d%H;%M:%S')
             filename="%s%s"%(current_time,old_name)
             return os.path.join('uploads/',filename)
     

        image = models.ImageField(upload_to=get_filename,null=True,blank=True)
        shopname = models.CharField(max_length=200)
        vendorname = models.CharField(max_length=200)
        phone     = models.CharField(max_length=200)
        description= models.CharField(max_length=2000)        
        location=models.CharField(max_length=200)
        category=models.CharField(max_length=200)
        availability=models.CharField(max_length=200)

class Customer(models.Model):
     def __str__(self):
          return self.firstname

     firstname = models.CharField(max_length=200)
     lastname  = models.CharField(max_length=200)
     location  = models.CharField(max_length=200)
     phone     = models.CharField(max_length=200)     