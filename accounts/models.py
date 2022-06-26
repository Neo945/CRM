from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    class TypeUser(models.TextChoices):
        MARKETING = 'MRK', _('Marketing')
        OPERATIONS = 'OPR', _('Opetration')
        SALES = 'SLS', _('Sales')
        PRESALES = 'PSLS', _('PreSales')
    
    email = models.EmailField(max_length=254, unique=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=TypeUser.choices, default=TypeUser.MARKETING)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Job(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    linkedin_url = models.URLField(null=True)
    requirements = models.TextField(null=True)
    image = models.ImageField(null=True)
    document = models.FileField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)