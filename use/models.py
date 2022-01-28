from django.db import models

# Create your models here.



class userregister(models.Model):
    def __str__(self):
        return self.email


    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    role = models.CharField(max_length=200)