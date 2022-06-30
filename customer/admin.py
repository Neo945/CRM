from django.contrib import admin
from .models import Client, Client_Job,Customer_Job,Customer,Linkedin

# Register your models here.
admin.site.register(Client)
admin.site.register(Client_Job)
admin.site.register(Customer_Job)
admin.site.register(Customer)
admin.site.register(Linkedin)