from django.db import models

# Create your models here.

class Worker(models.Model):

        def __str__(self):
             return self.firstname
           

        firstname = models.CharField(max_length=200)
        lastname  = models.CharField(max_length=200)
        phone     = models.CharField(max_length=200)
        description= models.CharField(max_length=2000)
        rate=models.FloatField()
        location=models.CharField(max_length=200)
        category=models.CharField(max_length=200)
        availability=models.CharField(max_length=200)
