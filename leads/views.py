from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from accounts.models import CompanyAccount, Job

from customer.models import Customer, Customer_Job
from leads.serializers import MarketingSerializer, OperationSerializer, PreSalesSerializer, SalesSerializer
from .models import Marketing, Sales, PreSales, Operation

# Create your views here.
@api_view(['GET'])
def marketing_leads(request):
    if request.user.is_authenticated:
        company = CompanyAccount.objects.get(user=request.user)
        jobs = Job.objects.filter(company=company)
        customers = Customer_Job.objects.filter(job__in=jobs)
        marketing = Marketing.objects.filter(customer__in=customers)
        return Response({ 'success': True, 'data': MarketingSerializer(marketing, many=True).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['GET'])
def sales_leads(request):
    if request.user.is_authenticated:
        company = CompanyAccount.objects.get(user=request.user)
        jobs = Job.objects.filter(company=company)
        customers = Customer_Job.objects.filter(job__in=jobs)
        sales = Sales.objects.filter(customer__in=customers)
        return Response({ 'success': True, 'data': SalesSerializer(sales, many=True).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })


@api_view(['GET'])
def psales_leads(request):
    if request.user.is_authenticated:
        company = CompanyAccount.objects.get(user=request.user)
        jobs = Job.objects.filter(company=company)
        customers = Customer_Job.objects.filter(job__in=jobs)
        psales = PreSales.objects.filter(customer__in=customers)
        return Response({ 'success': True, 'data': PreSalesSerializer(psales , many=True).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })


@api_view(['GET'])
def operations_leads(request):
    if request.user.is_authenticated:
        company = CompanyAccount.objects.get(user=request.user)
        jobs = Job.objects.filter(company=company)
        customers = Customer_Job.objects.filter(job__in=jobs)
        operations = Operation.objects.filter(customer__in=customers)
        return Response({ 'success': True, 'data': OperationSerializer(operations, many=True).data })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['POST'])
def move_to_marketing(request):
    if request.user.is_authenticated:
        customers = Customer.objects.filter(id=request.data['customer_job_id'])
        for customer in customers:
            Marketing.objects.create(customer=customer, description=request.data['description'], name=request.data['name'])
        return Response({ 'success': True, 'data': 'Customer moved to marketing' })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['POST'])
def move_to_sales(request):
    if request.user.is_authenticated:
        marketing = Marketing.objects.filter(id=request.data['marketing_id'])
        for market in marketing:
            Sales.objects.create(customer=market.customer, description=request.data['description'], name=request.data['name'])
        return Response({ 'success': True, 'data': 'Customer moved to sales' })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['POST'])
def move_to_psales(request):
    if request.user.is_authenticated:
        sales = Sales.objects.filter(id=request.data['sales_id'])
        for sale in sales:
            PreSales.objects.create(customer=sale.customer, description=request.data['description'], name=request.data['name'])
        return Response({ 'success': True, 'data': 'Customer moved to pre-sales' })

    return Response({ 'success': False, 'data': 'You are not authenticated' })

@api_view(['POST'])
def move_to_operations(request):
    if request.user.is_authenticated:
        psales = PreSales.objects.filter(id=request.data['psales_id'])
        for psale in psales:
            Operation.objects.create(customer=psale.customer, description=request.data['description'], name=request.data['name'])
        return Response({ 'success': True, 'data': 'Customer moved to operations' })
    return Response({ 'success': False, 'data': 'You are not authenticated' })

