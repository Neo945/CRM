from django.contrib import admin
from .models import Leads, MarketingLead,OperationLead, PreSalesLead,SalesLead,Profile

# Register your models here.
admin.site.register(Leads)
admin.site.register(MarketingLead)
admin.site.register(OperationLead)
admin.site.register(PreSalesLead)
admin.site.register(SalesLead)
admin.site.register(Profile)

