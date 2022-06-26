from django.db import models

class CMRCSS(models.Model):
    feedback = models.TextField(null=True)
    liked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
