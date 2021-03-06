from django.db import models

from leads.models import OperationLead

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    linkedin = models.ForeignKey('Linkedin', on_delete=models.CASCADE, null=True)
    job = models.ManyToManyField('accounts.Job', through='Customer_Job', related_name='jobcustomer')

    def __str__(self):
        return self.name

class Linkedin(models.Model):
    name = models.CharField(max_length=200, null=True)
    designation = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    requirement = models.TextField(null=True)
    linkedin_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.linkedin_url

class Client(models.Model):
    operations = models.ForeignKey(OperationLead, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    linkedin = models.ForeignKey('Linkedin', on_delete=models.CASCADE, null=True)
    job = models.ManyToManyField('accounts.Job', through='Client_Job', related_name='jobclient')

    def __str__(self):
        return self.name

class Client_Job(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    job = models.ForeignKey('accounts.Job', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Customer_Job(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    job = models.ForeignKey('accounts.Job', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
