from django.db import models

# Create your models here.
class Marketing(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    # source = models.CharField(max_length=200, null=True)
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    requirements = models.TextField(null=True)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Sales(models.Model):
    details = models.TextField(null=True)
    pricing = models.TextField(null=True)
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    marketing = models.ForeignKey('Marketing', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class PreSales(models.Model):
    details = models.TextField(null=True)
    date = models.DateField(null=True, auto_now=True)
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    sales = models.ForeignKey('Sales', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Operation(models.Model):
    details = models.TextField(null=True)
    status = models.CharField(max_length=200, null=True)
    pricing = models.TextField(null=True)
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    presales = models.ForeignKey('PreSales', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)