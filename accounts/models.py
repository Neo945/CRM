from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CompanyAccount(models.Model):
    # company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class Job(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    company = models.ForeignKey('CompanyAccount', on_delete=models.CASCADE, null=True)
    linkedin_url = models.URLField(null=True)
    requirements = models.TextField(null=True)
    image = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
