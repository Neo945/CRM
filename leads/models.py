from django.db import models

from accounts.models import Profile
from django.utils.translation import gettext_lazy as _

class Leads(models.Model):
    customer = models.OneToOneField('customer.Customer', on_delete=models.CASCADE, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_done = models.BooleanField(default=False)

def checkMRK(x):
    return Profile.objects.get(user=x).type == 'MRK'
class MarketingLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    leads = models.ForeignKey('Leads', on_delete=models.CASCADE)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, validators=[checkMRK])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_done = models.BooleanField(default=False)

    refered_by_name = models.CharField(max_length=200, null=True)
    refered_source = models.CharField(max_length=200, null=True)
    requirements = models.TextField(null=True)

def checkSLS(x):
    print(Profile.objects.get(user=x).type, x, Profile.objects.get(user=x))
    return Profile.objects.get(user=x).type == 'SLS'
class SalesLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, validators=[checkSLS])
    marketinglead = models.ForeignKey('MarketingLead', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_done = models.BooleanField(default=False)

    sales_details = models.TextField(null=True)
    sales_pricing = models.TextField(null=True)


def checkPSLS(x):
    return Profile.objects.get(user=x).type == 'PSLS'
class PreSalesLead(models.Model):
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, validators=[checkPSLS])
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    saleslead = models.ForeignKey('SalesLead', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_done = models.BooleanField(default=False)

    proposal_details = models.TextField(null=True)
    proposal_date = models.DateField(null=True)

def checkOPR(x):
    return Profile.objects.get(user=x).type == 'OPR'
class OperationLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    presaleslead = models.ForeignKey('PreSalesLead', on_delete=models.CASCADE)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, validators=[checkOPR])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    is_done = models.BooleanField(default=False)

    class Status(models.TextChoices):
        PENDING = 'PND', _('Pending')
        APPROVED = 'APR', _('Approved')
        REJECTED = 'RJT', _('Rejected')


    deal_details = models.TextField(null=True)
    deal_status = models.CharField(max_length=200, default='PND', choices=Status.choices)
    detail_pricing = models.TextField(null=True)