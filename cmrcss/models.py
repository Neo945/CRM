from django.db import models

# Create your models here.
class CMRCSS(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    requirements = models.TextField(null=True)
    feedback = models.TextField(null=True)
    detail = models.TextField(null=True)
    website = models.URLField(null=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
