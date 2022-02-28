from django.contrib import admin
from .models import Post, Worker,Supplier,Customer,product


admin.site.register(Worker)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(product)
admin.site.register(Post)
# admin.site.register(Workers)
# Register your models here.
