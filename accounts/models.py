from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
# from django.utils import timezone  
# from django.utils.translation import gettext_lazy as _  
# from .managers import CustomUserManager

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


# class CustomUser(AbstractBaseUser, PermissionsMixin):  
#     username = None  
#     email = models.EmailField(_('email_address'), unique=True, max_length = 200)  
#     date_joined = models.DateTimeField(default=timezone.now)  
#     is_staff = models.BooleanField(default=False)  
#     is_active = models.BooleanField(default=True)  

#     USERNAME_FIELD = 'email'  
#     REQUIRED_FIELDS = []  
#     objects = CustomUserManager()  

#     def has_perm(self, perm, obj=None):  
#         "Does the user have a specific permission?"  
#         return True
    
#     def is_staff(self):  
#         "Is the user a member of staff?"  
#         return self.staff  
  
#     @property  
#     def is_admin(self):  
#         "Is the user a admin member?"  
#         return self.admin  
  
#     def __str__(self):  
#         return self.email