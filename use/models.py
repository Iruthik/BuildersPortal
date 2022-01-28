from django.db import models

# Create your models here.


# Create your models here.
class item(models.Model):
    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.IntegerField()
    role = models.CharField(max_length=500)