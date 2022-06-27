import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import Job, Profile

from customer.models import Client, Customer
from leads.serializers import LeadsSerializer, MarketingCreateSerializer, MarketingSerializer, OperationCreateSerializer, OperationSerializer, PreSalesCreateSerializer, PreSalesSerializer, SalesCreateSerializer, SalesSerializer
from .models import Leads, MarketingLead, SalesLead, PreSalesLead, OperationLead
from cryptography.fernet import Fernet

# Create your views here.

# tested
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_leads(request, customerid):
    """
    Create a leads
    Endpoint: /api/v1/leads/create/lead/customer/<int:customerid>
    method: GET
    """
    if not Leads.objects.filter(customer=customerid).exists():
        leads = Leads.objects.create(customer=Customer.objects.get(id=customerid))
        return Response({'status': 'success', 'leads': LeadsSerializer(leads).data})
    return Response({"message": "Leads already exists"}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_leads(request, leadsid):
    """
    Get a lead by id
    Endpoint: /api/v1/leads/lead/<int:leadsid>
    method: GET
    """
    return Response({'status': 'success', 'data': LeadsSerializer(Leads.objects.get(id=leadsid)).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_leads_by_job(request, jobid):
    """
    Get all leads by job id
    Endpoint: /api/v1/leads/lead/job/<int:jobid>
    method: GET
    """
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_checked_leads_by_job(request, jobid):
    """
    Get all checked leads by job id
    Endpoint: /api/v1/leads/lead/moved/job/<int:jobid>
    method: GET
    """
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers).filter(is_done=True)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_leads_by_job(request, jobid):
    """
    Get all unchecked leads by job id
    Endpoint: /api/v1/leads/lead/not/moved/job/<int:jobid>
    method: GET
    """
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers).filter(is_done=False)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_marketing_leads(request, leadid):
    """
    Create a marketing leads
    method: POST
    Endpoint: /api/v1/create/market/<int:leadid>
    data:
    {
        'refered_by_name': Refered by name,
        'refered_source' : Refered source,
        'requirements': Requirements, 
    }
    """
    if Profile.objects.get(user=request.user).type != 'MRK':
        return Response({'status': 'Not Authorized'})
    leads = Leads.objects.filter(id=leadid)
    serializer = MarketingCreateSerializer(data=request.data)
    if serializer.is_valid() and leads.exists():
        lead=leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), leads=lead)
        lead.is_done = True
        lead.save()
        fernet = Fernet(settings.KEY)
        data = {
            'id': instance.id,
            'status': 'MRK',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New Sales Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success', "data": MarketingSerializer(instance).data})
        return Response({'status': 'success',"data": MarketingSerializer(instance).data})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_marketing_leads(request):
    """
    Create all marketing leads
    method: POST
    Endpoint: /api/v1/create/market/
    data:
    [{
        'lead' : Lead id,
        'refered_by_name': Refered by name,
        'refered_source' : Refered source,
        'requirements': Requirements, 
    }]
    """
    if Profile.objects.get(user=request.user).type != 'MRK':
        return Response({'status': 'Not Authorized'})
    for lead in request.data.get('leads'):
        leads = Leads.objects.filter(id=lead.lead)
        serializer = MarketingCreateSerializer(data=lead.data)
        if serializer.is_valid() and leads.exists():
            lead1=leads.first()
            instance = serializer.save(approved_by=Profile.objects.get(user=request.user), lead=lead1)
            lead1.is_done = True
            lead1.save()
            fernet = Fernet(settings.KEY)
            data = {
                'id': instance.id,
                'status': 'MRK',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New Sales Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success', "data": MarketingSerializer(instance).data})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_marketing_leads(request, marketingleadid):
    """
    Get marketing lead by id
    Endpoint: /api/v1/leads/market/<int:marketingleadid>
    method: GET
    """
    return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.get(id=marketingleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_marketing_leads(request):
    """
    Get all marketing leads
    Endpoint: /api/v1/leads/market/
    method: POST
    {
        'marketing': [list of marketing lead ids]
    }
    """
    return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_marketing_leads(request):
    """
    Get all checked marketing leads
    Endpoint: /api/v1/leads/market/moved/
    method: POST
    {
        'marketing': [list of marketing lead ids]
    }
    """
    if request.method == 'POST':
        return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=True), many=True).data})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_marketing_leads(request):
    """
    Get all unchecked marketing leads
    Endpoint: /api/v1/leads/market/not/moved/
    method: POST
    {
        'marketing': [list of marketing lead ids]
    }
    """
    return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=False), many=True).data})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_marketing_leads_by_job(request, jobid):
    """
    Get all marketing leads by job id
    Endpoint: /api/v1/leads/market/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_marketing_leads_by_job(request, jobid):
    """
    Get all checked marketing leads by job id
    Endpoint: /api/v1/leads/market/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(lead__in=leads).filter(is_done=True)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_marketing_leads_by_job(request, jobid):
    """
    Get all unchecked marketing leads by job id
    Endpoint: /api/v1/leads/market/not/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(lead__in=leads).filter(is_done=False)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sales_leads(request, marketingleadid):
    """
    Create a sales leads
    method: POST
    Endpoint: /api/v1/leads/create/sales/<int:marketingleadid>
    data:
    {
        'sales_details': Sales details,
        'sales_pricing' : Sales pricing,
    }
    """
    if Profile.objects.get(user=request.user).type != 'SLS':
        return Response({'status': 'Not Authorized'})
    leads = MarketingLead.objects.filter(id=marketingleadid)
    serializer = SalesCreateSerializer(data=request.data)
    if serializer.is_valid() and leads.exists():
        lead = leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), marketinglead=lead)
        lead.is_done = True
        lead.save()
        fernet = Fernet(settings.KEY)
        data = {
            'id': instance.id,
            'status': 'SLS',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New Sales Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.leads.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_sales_leads(request):
    """
    Create all sales leads
    method: POST
    Endpoint: /api/v1/leads/create/sales/
    data:
    [{
        'lead' : MarketingLead id,
        'sales_details': Sales details,
        'sales_pricing' : Sales pricing,
    }]
    """
    if Profile.objects.get(user=request.user).type != 'SLS':
        return Response({'status': 'Not Authorized'})
    for lead in request.data.get('leads'):
        leads = MarketingLead.objects.filter(id=lead.lead)
        serializer = SalesCreateSerializer(data=lead.data)
        if serializer.is_valid() and leads.exists():
            lead1=leads.first()
            instance = serializer.save(approved_by=Profile.objects.get(user=request.user), marketinglead=lead1)
            lead1.is_done = True
            lead1.save()
            fernet = Fernet(settings.KEY)
            data = {
                'id': instance.id,
                'status': 'SLS',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New Sales Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.leads.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sales_leads(request, salesleadid):
    """
    Get sales lead by id
    Endpoint: /api/v1/leads/sales/<int:salesleadid>
    method: GET
    """
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.get(id=salesleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_sales_leads(request):
    """
    Get all sales leads
    Endpoint: /api/v1/leads/sales/
    method: POST
    {
        'sales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('sales')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_sales_leads(request):
    """
    Get all checked sales leads
    Endpoint: /api/v1/leads/sales/moved/
    method: POST
    {
        'sales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('sales')).filter(is_done=True), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_sales_leads(request):
    """
    Get all unchecked sales leads
    Endpoint: /api/v1/leads/sales/not/moved/
    method: POST
    {
        'sales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('sales')).filter(is_done=False), many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sales_leads_by_job(request, jobid):
    """
    Get all sales leads by job id
    Endpoint: /api/v1/leads/sales/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_sales_leads_by_job(request, jobid):
    """
    Get all checked sales leads by job id
    Endpoint: /api/v1/leads/sales/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads).filter(is_done=True)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_sales_leads_by_job(request, jobid):
    """
    Get all unchecked sales leads by job id
    Endpoint: /api/v1/leads/sales/not/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads).filter(is_done=False)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_presales_leads(request, salesleadid):
    """
    Create a presales leads
    method: POST
    Endpoint: /api/v1/create/presales/<int:salesleadid>
    data:
    {
        'proposal_details': Proposal details,
        'proposal_date' : Proposal date,
    }
    """
    if Profile.objects.get(user=request.user).type != 'PSLS':
        return Response({'status': 'Not Authorized'})
    leads = SalesLead.objects.filter(id=salesleadid)
    serializer = PreSalesCreateSerializer(data=request.data)
    if serializer.is_valid() and leads.exists():
        lead = leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), saleslead=lead)
        lead.is_done = True
        lead.save()
        fernet = Fernet(settings.KEY)
        data = {
            'id': instance.id,
            'status': 'PSLS',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New PreSales Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.marketinglead.leads.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_presales_leads(request):
    """
    Create all presales leads
    method: POST
    Endpoint: /api/v1/create/presales/
    data:
    [{
        'lead' : Sales id,
        'proposal_details': Proposal details,
        'proposal_date' : Proposal date,
    }]
    """
    if Profile.objects.get(user=request.user).type != 'SLS':
        return Response({'status': 'Not Authorized'})
    for lead in request.data.get('leads'):
        leads = SalesLead.objects.filter(id=lead.lead)
        serializer = PreSalesCreateSerializer(data=lead.data)
        if serializer.is_valid() and leads.exists():
            lead1 = leads.first()
            instance = serializer.save(approved_by=Profile.objects.get(user=request.user), saleslead=lead1)
            lead1.is_done = True
            lead1.save()
            fernet = Fernet(settings.KEY)
            data = {
                'id': instance.id,
                'status': 'PSLS',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New PreSales Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.marketinglead.leads.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_presales_leads(request, presalesleadid):
    """
    Get presales lead by id
    Endpoint: /api/v1/leads/presales/<int:presalesleadid>
    method: GET
    """
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.get(id=presalesleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_presales_leads(request):
    """
    Get all presales leads
    Endpoint: /api/v1/leads/presales/
    method: POST
    {
        'presales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_presales_leads(request):
    """
    Get all checked presales leads
    Endpoint: /api/v1/leads/presales/moved/
    method: POST
    {
        'presales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')).filter(is_done=True), many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_presales_leads(request):
    """
    Get all unchecked presales leads
    Endpoint: /api/v1/leads/presales/not/moved/
    method: POST
    {
        'presales': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')).filter(is_done=False), many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_presales_leads_by_job(request, jobid):
    """
    Get all presales leads by job id
    Endpoint: /api/v1/leads/presales/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_presales_leads_by_job(request, jobid):
    """
    Get all checked presales leads by job id
    Endpoint: /api/v1/leads/presales/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads).filter(is_done=True)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_presales_leads_by_job(request, jobid):
    """
    Get all unchecked presales leads by job id
    Endpoint: /api/v1/leads/presales/not/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads).filter(is_done=False)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_operation_leads(request, presalesleadid):
    """
    Create a operation leads
    method: POST
    Endpoint: /api/v1/create/operation/<int:presalesleadid>
    data:
    {
        'deal_details': Deal Details,
        'deal_status' : Deal Status,
        'detail_pricing' : Detail Pricing,
    }
    """
    if Profile.objects.get(user=request.user).type != 'OPR':
        return Response({'status': 'Not Authorized'})
    leads = PreSalesLead.objects.filter(id=presalesleadid)
    serializer = OperationCreateSerializer(data=request.data)
    print(serializer.is_valid())
    print(serializer.errors)
    print(leads.exists())
    if serializer.is_valid() and leads.exists():
        lead = leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), presaleslead=lead)
        lead.is_done = True
        lead.save()
        fernet = Fernet(settings.KEY)
        data = {
            'id': instance.id,
            'status': 'OPR',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New Operation Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.saleslead.marketinglead.leads.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_operations_leads(request):
    """
    Create all operation leads
    method: POST
    Endpoint: /api/v1/create/operation/
    data:
    [{
        'lead': Presales lead,
        'deal_details': Deal Details,
        'deal_status' : Deal Status,
        'detail_pricing' : Detail Pricing,
    }]
    """
    if Profile.objects.get(user=request.user).type != 'OPR':
        return Response({'status': 'Not Authorized'})
    for lead in request.data.get('leads'):
        leads = OperationLead.objects.filter(id=lead.lead)
        serializer = OperationCreateSerializer(data=lead.data)
        if serializer.is_valid() and leads.exists():
            lead1 = leads.first()
            instance = serializer.save(approved_by=Profile.objects.get(user=request.user), presaleslead=lead1)
            lead1.is_done = True
            lead1.save()
            fernet = Fernet(settings.KEY)
            data = {
                'id': instance.id,
                'status': 'OPR',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New Operation Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/api/v1/cmrcss/feedback/" + str(token.decode()) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.saleslead.marketinglead.lead.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_operations_leads(request, opeartionsleadid):
    """
    Get Operation lead by id
    Endpoint: /api/v1/leads/operation/<int:opeartionsleadid>
    method: GET
    """
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.get(id=opeartionsleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_operations_leads(request):
    """
    Get all operation leads
    Endpoint: /api/v1/leads/operation/
    method: POST
    {
        'operation': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operation')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_operations_leads(request):
    """
    Get all checked operation leads
    Endpoint: /api/v1/leads/operation/moved/
    method: POST
    {
        'operation': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operation')).filter(is_done=True), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_operations_leads(request):
    """
    Get all unchecked operation leads
    Endpoint: /api/v1/leads/operation/not/moved/
    method: POST
    {
        'operation': [list of sales lead ids]
    }
    """
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operation')).filter(is_done=False), many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_operations_leads_by_job(request, jobid):
    """
    Get all operation leads by job id
    Endpoint: /api/v1/leads/operation/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads)
    operationsleads = OperationLead.objects.filter(presaleslead__in=presalesleads)
    return Response({'status': 'success', 'data': OperationSerializer(operationsleads, many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_operations_leads_by_job(request, jobid):
    """
    Get all checked operation leads by job id
    Endpoint: /api/v1/leads/operation/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads)
    operationsleads = OperationLead.objects.filter(presaleslead__in=presalesleads).filter(is_done=True)
    return Response({'status': 'success', 'data': OperationSerializer(operationsleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_operations_leads_by_job(request, jobid):
    """
    Get all unchecked operation leads by job id
    Endpoint: /api/v1/leads/operation/not/moved/job/<int:jobid>
    method: GET
    """
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(saleslead__in=salesleads)
    operationsleads = OperationLead.objects.filter(presaleslead__in=presalesleads).filter(is_done=False)
    return Response({'status': 'success', 'data': OperationSerializer(operationsleads, many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_client_from_operations(request, operationsleadid, jobid):
    """
    Create client from operations lead
    Endpoint: /api/v1/leads/create/client/operation/<int:operationsleadid>/job/<int:jobid>
    method: GET
    """
    if Profile.objects.get(user=request.user).type != 'OPR':
        return Response({'status': 'Not Authorized'})
    operationslead = OperationLead.objects.get(id=operationsleadid)
    client = Client.objects.create(
        operations=operationslead,
        name=operationslead.presaleslead.saleslead.marketinglead.leads.customer.name,
        phone=operationslead.presaleslead.saleslead.marketinglead.leads.customer.phone,
        email=operationslead.presaleslead.saleslead.marketinglead.leads.customer.email,
        website=operationslead.presaleslead.saleslead.marketinglead.leads.customer.website,
        description=operationslead.presaleslead.saleslead.marketinglead.leads.customer.description,
        linkedin=operationslead.presaleslead.saleslead.marketinglead.leads.customer.linkedin,
    )
    subject = 'Whole feedback'
    message = "Congratulations! You have been selected as a client for the job: " + Job.objects.get(id=jobid).name + ".\n\n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [operationslead.presaleslead.saleslead.marketinglead.leads.customer.email]
    send_mail( subject, message, email_from, recipient_list )
    operationslead.is_done = True
    operationslead.deal_status = 'APR'
    operationslead.save()
    client.job.add(Job.objects.get(id=jobid))
    client.save()
    return Response({'status': 'success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_client_from_operations(request, jobid):
    """
    Create all client from operations lead
    Endpoint: /api/v1/leads/create/client/job/<int:jobid>
    method: POST
    {
        'operationsleads': [list of operations lead ids]
    }
    """
    for lead in request.data.get('operationsleads'):
        operationslead = OperationLead.objects.get(id=lead)
        subject = 'Whole feedback'
        message = "Congratulations! You have been selected as a client for the job: " + Job.objects.get(id=jobid).name + ".\n\n"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [operationslead.presaleslead.saleslead.marketinglead.lead.customer.email]
        send_mail( subject, message, email_from, recipient_list )
        operationslead.is_done = True
        operationslead.save()
        client = Client.objects.create(
            operations=operationslead,
            name=operationslead.presaleslead.saleslead.marketinglead.lead.customer.name,
            phone=operationslead.presaleslead.saleslead.marketinglead.lead.customer.phone,
            email=operationslead.presaleslead.saleslead.marketinglead.lead.customer.email,
            website=operationslead.presaleslead.saleslead.marketinglead.lead.customer.website,
            description=operationslead.presaleslead.saleslead.marketinglead.lead.customer.description,
            linkedin=operationslead.presaleslead.saleslead.marketinglead.lead.customer.linkedin,
        )
        client.job.add(Job.objects.get(id=jobid))
        client.save()
    return Response({'status': 'success'})
