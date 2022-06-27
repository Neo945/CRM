from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import urllib.request
from django.core.mail import EmailMessage
from accounts.models import Job
from customer.serializers import  CustomerCreateSerializer, CustomerSerializer, LinkedinSerializer
from django.conf import settings
from django.core.mail import send_mail

from leads.serializers import ClientSerializer

from .models import Client, Customer

#tested
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer(request, customerid):
    """
    Get a customer by id
    method: GET
    Endpoint: /api/v1/customer/get/<int:customerid>
    """
    if request.user.is_authenticated:
        costomer = Customer.objects.get(user=customerid)
        return Response({ 'success': True, 'data': CustomerSerializer(costomer).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_customer(request):
    """
    Create a customer
    method: POST
    Endpoint: /api/v1/customer/create/customer/
    data:
    {
        'name': customer name, 
        'phone': customer phone,, 
        'email' : customer email,, 
        'website': customer website,, 
        'description': customer description,
        "designation" : customer designation,
        "company" : customer company,
        "requirement" : customer requirement,
        'linkedin_url': customer linkedin url,
    }
    """
    serializer = CustomerCreateSerializer(data=request.data)
    linkedin_serializer = LinkedinSerializer(data=request.data)
    if serializer.is_valid() and linkedin_serializer.is_valid():
        linkedin = linkedin_serializer.save()
        customer = serializer.save(linkedin=linkedin)
        print(customer)
        if not request.data.get('job'):
            return Response({ 'success': True })
        job = Job.objects.get(id=request.data['job'])
        if customer.job.filter(id=job).exists():
            return Response({ 'success': False, 'data': 'Customer already added to job' })
        customer.job.add(job)
        subject = "Show some interest"
        response = urllib.request.urlopen(job.document)
        message = f"Click here to see the job <a href='https://127.0.0.1:8000/api/v1/leads/create/lead/customer/{customer.id}'>{customer.name}</a>"
        recipient_list = [customer.email]
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        mail.content_subtype = "html"
        mail.attach("Attachments.pdf", response.read(), "application/pdf")
        if send_mail( subject, message, settings.EMAIL_HOST_USER, recipient_list ) != 0:
            return Response({"message":"Email sent successfully", 'data': CustomerSerializer(customer).data, "sucess": True}, status=200)
        return Response({ 'success': True, "message": "Not able to send email but data saved", 'data': CustomerSerializer(customer).data })
    return Response({ 'success': False, 'data': serializer.errors })

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def add_customer_to_job(request, customerid, jobid):
    """
    Add a customer to a job
    method: GET
    Endpoint: /api/v1/customer/add/customer/<int:customerid>/job/<int:jobid>
    """
    customer = Customer.objects.get(id=customerid)
    job = Job.objects.get(id=jobid)
    if customer.job.filter(id=jobid).exists():
        return Response({ 'success': False, 'data': 'Customer already added to job' })
    customer.job.add(job)
    subject = "Show some interest"
    response = urllib.request.urlopen(job.document)
    message = f"Click here to see the job <a href='https://127.0.0.1:8000/api/v1/leads/create/lead/customer/{customer.id}'>{customer.name}</a>"
    recipient_list = [customer.email]
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    # mail.content_subtype = "html"
    mail.attach("Attachments.pdf", response.read(), "application/pdf")
    if mail.send() != 0:
        return Response({"message":"Email sent successfully", 'data': CustomerSerializer(customer).data, "sucess": True}, status=200)
    return Response({ 'success': True, 'data': 'Customer added to job' })


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_customer_by_job(request, jobid):
    """
    Get a customer by job id
    method: GET
    Endpoint: /api/v1/customer/get/job/<int:jobid>
    """
    customers = Customer.objects.filter(job=jobid)
    return Response({ 'success': True, 'data': CustomerSerializer(customers, many=True).data })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_clients_by_job(request, jobid):
    """
    Get a client by job id
    method: GET
    Endpoint: /api/v1/customer/get/client/job/<int:jobid>
    """

    client = Client.objects.filter(job=jobid)
    return Response({ 'success': True, 'data': ClientSerializer(client, many=True).data })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_client(request, clientid):
    """
    Get a customer by id
    method: GET
    Endpoint: /api/v1/customer/get/client/<int:clientid>
    """
    client = Client.objects.filter(id=clientid)
    return Response({ 'success': True, 'data': ClientSerializer(client).data })
