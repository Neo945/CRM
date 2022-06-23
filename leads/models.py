from django.db import models

from accounts.models import Profile
from django.utils.translation import gettext_lazy as _

class Leads(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

class MarketingLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    leads = models.ForeignKey('Leads', on_delete=models.CASCADE, null=True)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, validators=[lambda x: Profile.objects.get(user=x).type == 'MRK'])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    refered_by_name = models.CharField(max_length=200, null=True)
    refered_source = models.CharField(max_length=200, null=True)
    requirements = models.TextField(null=True)

class SalesLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, validators=[lambda x: Profile.objects.get(user=x).type == 'SLS'])
    marketinglead = models.ForeignKey('MarketingLead', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    sales_details = models.TextField(null=True)
    sales_pricing = models.TextField(null=True)

class PreSalesLead(models.Model):
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, validators=[lambda x: Profile.objects.get(user=x).type == 'PSLS'])
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    saleslead = models.ForeignKey('SalesLead', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    proposal_details = models.TextField(null=True)
    proposal_date = models.DateField(null=True)

class OperationLead(models.Model):
    cmrcss = models.ForeignKey('cmrcss.CMRCSS', on_delete=models.CASCADE, null=True)
    presaleslead = models.ForeignKey('PreSalesLead', on_delete=models.CASCADE, null=True)
    approved_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True, validators=[lambda x: Profile.objects.get(user=x).type == 'OPR'])
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Status(models.TextChoices):
        PENDING = 'PND', _('Pending')
        APPROVED = 'APR', _('Approved')
        REJECTED = 'RJT', _('Rejected')


    deal_details = models.TextField(null=True)
    deal_status = models.CharField(max_length=200, null=True, choices=Status.choices)
    detail_pricing = models.TextField(null=True)