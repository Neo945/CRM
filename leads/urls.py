from django.urls import path

from leads.views import create_all_client_from_operations, create_all_marketing_leads, create_all_operations_leads, create_all_presales_leads, create_all_sales_leads, create_client_from_operations, create_leads, create_marketing_leads, create_operation_leads, create_presales_leads, create_sales_leads, get_all_checked_leads_by_job, get_all_checked_marketing_leads, get_all_checked_operations_leads, get_all_checked_presales_leads, get_all_checked_sales_leads, get_all_leads_by_job, get_all_marketing_leads, get_all_operations_leads, get_all_presales_leads, get_all_sales_leads, get_all_unchecked_leads_by_job, get_all_unchecked_marketing_leads, get_all_unchecked_operations_leads, get_all_unchecked_presales_leads, get_all_unchecked_sales_leads, get_checked_marketing_leads_by_job, get_checked_operations_leads_by_job, get_checked_presales_leads_by_job, get_checked_sales_leads_by_job, get_leads, get_marketing_leads, get_marketing_leads_by_job, get_operations_leads, get_operations_leads_by_job, get_presales_leads, get_presales_leads_by_job, get_sales_leads, get_sales_leads_by_job, get_unchecked_marketing_leads_by_job, get_unchecked_operations_leads_by_job, get_unchecked_presales_leads_by_job, get_unchecked_sales_leads_by_job

app_name = 'leads'

urlpatterns = [
    path('create/lead/customer/<int:customerid>', create_leads, name='create_leads'),
    path('lead/<int:leadsid>', get_leads, name='get_leads'),
    path('lead/job/<int:jobid>', get_all_leads_by_job,name='get_all_leads_by_job'),
    path('lead/moved/job/<int:jobid>', get_all_checked_leads_by_job,name='get_all_checked_leads_by_job'),
    path('lead/not/moved/job/<int:jobid>', get_all_unchecked_leads_by_job,name='get_all_checked_leads_by_job'),
    path('create/market/<int:leadid>', create_marketing_leads, name='create_marketing_leads'),
    path('create/market/', create_all_marketing_leads, name='create_all_marketing_leads'),
    path('market/<int:marketingleadid>', get_marketing_leads, name='get_marketing_leads'),
    path('market/', get_all_marketing_leads, name='get_all_marketing_leads'),
    path('market/moved/', get_all_checked_marketing_leads, name='get_all_checked_marketing_leads'),
    path('market/not/moved/', get_all_unchecked_marketing_leads, name='get_all_unchecked_marketing_leads'),
    path('market/job/<int:jobid>', get_marketing_leads_by_job, name='get_marketing_leads_by_job'),
    path('market/moved/job/<int:jobid>', get_checked_marketing_leads_by_job, name='get_marketing_leads_by_job'),
    path('market/not/moved/job/<int:jobid>', get_unchecked_marketing_leads_by_job, name='get_marketing_leads_by_job'),

    path('create/sales/<int:marketingleadid>', create_sales_leads, name='create_sales_leads'),
    path('create/sales/', create_all_sales_leads, name='create_all_sales_leads'),
    path('sales/<int:salesleadid>', get_sales_leads, name='get_sales_leads'),
    path('sales/', get_all_sales_leads, name='get_all_sales_leads'),
    path('sales/job/<int:jobid>', get_sales_leads_by_job, name='get_sales_leads_by_job'),
    path('sales/moved/', get_all_checked_sales_leads, name='get_all_checked_marketing_leads'),
    path('sales/not/moved/', get_all_unchecked_sales_leads, name='get_all_unchecked_marketing_leads'),
    path('sales/moved/job/<int:jobid>', get_checked_sales_leads_by_job, name='get_marketing_leads_by_job'),
    path('sales/not/moved/job/<int:jobid>', get_unchecked_sales_leads_by_job, name='get_marketing_leads_by_job'),

    path('create/presales/<int:salesleadid>', create_presales_leads, name='create_presales_leads'),
    path('create/presales/', create_all_presales_leads, name='create_all_presales_leads'),
    path('presales/<int:presalesleadid>', get_presales_leads, name='get_presales_leads'),
    path('presales/', get_all_presales_leads, name='get_all_presales_leads'),
    path('presales/job/<int:jobid>', get_presales_leads_by_job, name='get_presales_leads_by_job'),
    path('presales/moved/', get_all_checked_presales_leads, name='get_all_checked_marketing_leads'),
    path('presales/not/moved/', get_all_unchecked_presales_leads, name='get_all_unchecked_marketing_leads'),
    path('presales/moved/job/<int:jobid>', get_checked_presales_leads_by_job, name='get_marketing_leads_by_job'),
    path('presales/not/moved/job/<int:jobid>', get_unchecked_presales_leads_by_job, name='get_marketing_leads_by_job'),

    path('create/operation/<int:presalesleadid>', create_operation_leads, name='create_operation_leads'),
    path('create/operation/', create_all_operations_leads, name='create_all_operation_leads'),
    path('operation/<int:opeartionsleadid>', get_operations_leads, name='get_operations_leads'),
    path('operation/', get_all_operations_leads, name='get_all_operations_leads'),
    path('operation/job/<int:jobid>', get_operations_leads_by_job, name='get_operations_leads_by_job'),
    path('presales/moved/', get_all_checked_operations_leads, name='get_all_checked_marketing_leads'),
    path('presales/not/moved/', get_all_unchecked_operations_leads, name='get_all_unchecked_marketing_leads'),
    path('presales/moved/job/<int:jobid>', get_checked_operations_leads_by_job, name='get_marketing_leads_by_job'),
    path('presales/not/moved/job/<int:jobid>', get_unchecked_operations_leads_by_job, name='get_marketing_leads_by_job'),

    path('create/client/operation/<int:operationsleadid>/job/<int:jobid>', create_client_from_operations, name='create_client_from_operations'),
    path('create/client/job/<int:jobid>', create_all_client_from_operations, name='create_all_client_from_operations'),
]