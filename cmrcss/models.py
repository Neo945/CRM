from django.db import models

from customer.models import Customer

# Create your models here.
class CMRCSS(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    feedback = models.TextField(null=True)
    liked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
