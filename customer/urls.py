from django.urls import path

from customer.views import add_customer_to_job, create_customer, get_client, get_clients_by_job, get_customer, get_customer_by_job

app_name = 'customer'

urlpatterns = [
    path('get/<int:customerid>', get_customer, name='get_customer'),
    path('create/customer/', create_customer, name='create_customer'),
    path('add/customer/<int:customerid>/job/<int:jobid>', add_customer_to_job, name='add_customer_to_job'),
    path('get/job/<int:jobid>', get_customer_by_job, name='get_customer_by_job'),
    path('get/client/<int:clientid>', get_client, name='get_client'),
    path('get/client/job/<int:jobid>', get_clients_by_job, name='get_clients_by_job'),
]