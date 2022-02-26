from django.contrib import admin
from .models import Worker,Supplier,Customer, Workers


admin.site.register(Worker)
admin.site.register(Supplier)
admin.site.register(Customer)

admin.site.register(Workers)
# Register your models here.
