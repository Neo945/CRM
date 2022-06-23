from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from accounts.models import CompanyAccount, Job
from customer.serializers import AccountSerializer, CustomerSerializer

from .models import Account, Customer, Customer_Job, Account_Company,Linkedin

# Create your views here.
@api_view(['GET'])
def get_customer(request,customerid):
    if request.user.is_authenticated:
        costomer = Customer.objects.get(user=customerid)
        return Response({ 'success': True, 'data': CustomerSerializer(costomer).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['GET'])
def create_account(request,customerid):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=customerid)
        account = Account.objects.create(customer=customer, name=customer.name, phone=customer.phone, email=customer.email, website=customer.website, address=customer.address, description=customer.description, linkedin=customer.linkedin)
        return Response({ 'success': True, 'data': AccountSerializer(account).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })
