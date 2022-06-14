from django.db import models

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

class Account(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    operation = models.ForeignKey('leads.Operation', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    linkedin = models.ForeignKey('Linkedin', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Account_Company(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE, null=False)
    job = models.ForeignKey('accounts.Job', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Customer_Job(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=False)
    job = models.ForeignKey('accounts.Job', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
