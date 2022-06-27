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
    if not Leads.objects.filter(customer=customerid).exists():
        leads = Leads.objects.create(customer=Customer.objects.get(id=customerid))
        return Response({'status': 'success', 'leads': LeadsSerializer(leads).data})
    return Response({"message": "Leads already exists"}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_leads(request, leadsid):
    return Response({'status': 'success', 'data': LeadsSerializer(Leads.objects.get(id=leadsid)).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_leads_by_job(request, jobid):
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_checked_leads_by_job(request, jobid):
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers).filter(is_done=True)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_leads_by_job(request, jobid):
    costumers = Customer.objects.filter(job=jobid)
    if costumers.exists():
        leads = Leads.objects.filter(customer__in=costumers).filter(is_done=False)
        return Response({'status': 'success', 'data': LeadsSerializer(leads, many=True).data}, status=200)
    return Response({'status': 'unsuccess',"data": []}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_marketing_leads(request, leadid):
    if Profile.objects.get(user=request.user).type != 'MRK':
        return Response({'status': 'Not Authorized'})
    leads = Leads.objects.filter(id=leadid)
    serializer = MarketingCreateSerializer(data=request.data)
    if serializer.is_valid() and leads.exists():
        lead=leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), leads=lead)
        lead.is_done = True
        lead.save()
        subject = 'Moving to marketing team'
        message = "Moving to next stage"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success', "data": MarketingSerializer(instance).data})
        return Response({'status': 'success',"data": MarketingSerializer(instance).data})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_marketing_leads(request):
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
            subject = 'New Marketing Feedback'
            message = "Moving to next stage"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success', "data": MarketingSerializer(instance).data})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_marketing_leads(request, marketingleadid):
    return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.get(id=marketingleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_marketing_leads(request):
    return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_marketing_leads(request):
    if request.method == 'POST':
        return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=True), many=True).data})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_marketing_leads(request):
    if request.method == 'POST':
        return Response({'status': 'success', 'data': MarketingSerializer(MarketingLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=False), many=True).data})
    return Response({'status': 'failure'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_marketing_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_marketing_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(lead__in=leads).filter(is_done=True)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_marketing_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(lead__in=leads).filter(is_done=False)
    return Response({'status': 'success', 'data': MarketingSerializer(marketingleads, many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sales_leads(request, marketingleadid):
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
            'status': 'MRK',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New Sales Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.leads.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_sales_leads(request):
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
                'status': 'MRK',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New Sales Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.leads.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sales_leads(request, salesleadid):
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.get(id=salesleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_sales_leads(request):
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('marketing')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_sales_leads(request):
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=True), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_sales_leads(request):
    return Response({'status': 'success', 'data': SalesSerializer(SalesLead.objects.filter(id__in=request.data.get('marketing')).filter(is_done=False), many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_sales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads).filter(is_done=True)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_sales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads).filter(is_done=False)
    return Response({'status': 'success', 'data': SalesSerializer(salesleads, many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_presales_leads(request, salesleadid):
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
            'status': 'SLS',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New PreSales Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.marketinglead.leads.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_presales_leads(request):
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
                'status': 'SLS',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New PreSales Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.marketinglead.leads.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_presales_leads(request, presalesleadid):
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.get(id=presalesleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_presales_leads(request):
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_presales_leads(request):
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')).filter(is_done=True), many=True).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_presales_leads(request):
    return Response({'status': 'success', 'data': PreSalesSerializer(PreSalesLead.objects.filter(id__in=request.data.get('presales')).filter(is_done=False), many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_presales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(marketinglead__in=salesleads)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_checked_presales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(marketinglead__in=salesleads).filter(is_done=True)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_unchecked_presales_leads_by_job(request, jobid):
    job = Job.objects.get(id=jobid)
    customers = Customer.objects.filter(job=job)
    leads = Leads.objects.filter(customer__in=customers)
    marketingleads = MarketingLead.objects.filter(leads__in=leads)
    salesleads = SalesLead.objects.filter(marketinglead__in=marketingleads)
    presalesleads = PreSalesLead.objects.filter(marketinglead__in=salesleads).filter(is_done=False)
    return Response({'status': 'success', 'data': PreSalesSerializer(presalesleads, many=True).data})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_operation_leads(request, presalesleadid):
    if Profile.objects.get(user=request.user).type != 'OPR':
        return Response({'status': 'Not Authorized'})
    leads = PreSalesLead.objects.filter(id=presalesleadid)
    serializer = OperationCreateSerializer(data=request.data)
    if serializer.is_valid() and leads.exists():
        lead = leads.first()
        instance = serializer.save(approved_by=Profile.objects.get(user=request.user), presaleslead=lead)
        lead.is_done = True
        lead.save()
        fernet = Fernet(settings.KEY)
        data = {
            'id': instance.id,
            'status': 'PSLS',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'New Operation Feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [lead.saleslead.marketinglead.lead.customer.email]
        if send_mail( subject, message, email_from, recipient_list ):
            return Response({'status': 'success'})
        return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_operations_leads(request):
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
                'status': 'PSLS',
            }
            token = fernet.encrypt(json.dumps(data).encode())
            subject = 'New Operation Feedback'
            message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [lead1.saleslead.marketinglead.lead.customer.email]
            if send_mail( subject, message, email_from, recipient_list ):
                return Response({'status': 'success'})
            return Response({'status': 'success'})
    return Response({'status': 'failure'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_operations_leads(request, opeartionsleadid):
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.get(id=opeartionsleadid)).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_operations_leads(request):
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operations')), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_checked_operations_leads(request):
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operations')).filter(is_done=True), many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_all_unchecked_operations_leads(request):
    return Response({'status': 'success', 'data': OperationSerializer(PreSalesLead.objects.filter(id__in=request.data.get('operations')).filter(is_done=False), many=True).data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_operations_leads_by_job(request, jobid):
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
    if Profile.objects.get(user=request.user).type != 'OPR':
        return Response({'status': 'Not Authorized'})
    operationslead = OperationLead.objects.get(id=operationsleadid)
    fernet = Fernet(settings.KEY)
    data = {
        'id': operationslead.id,
        'status': 'OPR',
    }
    token = fernet.encrypt(json.dumps(data).encode())
    subject = 'Whole feedback'
    message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [operationslead.presaleslead.saleslead.marketinglead.lead.customer.email]
    send_mail( subject, message, email_from, recipient_list )
    client = Client.objects.create(
        operations_account=operationslead.id,
        name=operationslead.presaleslead.saleslead.marketinglead.lead.customer.name,
        phone=operationslead.presaleslead.saleslead.marketinglead.lead.customer.phone,
        email=operationslead.presaleslead.saleslead.marketinglead.lead.customer.email,
        website=operationslead.presaleslead.saleslead.marketinglead.lead.customer.website,
        description=operationslead.presaleslead.saleslead.marketinglead.lead.customer.description,
        linkedin=operationslead.presaleslead.saleslead.marketinglead.lead.customer.linkedin,
    )
    operationslead.is_done = True
    operationslead.save()
    client.jobs.add(Job.objects.get(id=jobid))
    client.save()
    return Response({'status': 'success'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_all_client_from_operations(request, jobid):
    for lead in request.data.get('operationsleads'):
        operationslead = OperationLead.objects.get(id=lead)
        fernet = Fernet(settings.KEY)
        data = {
            'id': operationslead.id,
            'status': 'OPR',
        }
        token = fernet.encrypt(json.dumps(data).encode())
        subject = 'Whole feedback'
        message = "Please give us your feedback on the customer. <a href='http://localhost:8000/customer/feedback/" + str(token) + "'>Click here to give feedback</a>"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [operationslead.presaleslead.saleslead.marketinglead.lead.customer.email]
        send_mail( subject, message, email_from, recipient_list )
        operationslead.is_done = True
        operationslead.save()
        client = Client.objects.create(
            operations_account=operationslead.id,
            name=operationslead.presaleslead.saleslead.marketinglead.lead.customer.name,
            phone=operationslead.presaleslead.saleslead.marketinglead.lead.customer.phone,
            email=operationslead.presaleslead.saleslead.marketinglead.lead.customer.email,
            website=operationslead.presaleslead.saleslead.marketinglead.lead.customer.website,
            description=operationslead.presaleslead.saleslead.marketinglead.lead.customer.description,
            linkedin=operationslead.presaleslead.saleslead.marketinglead.lead.customer.linkedin,
        )
        client.jobs.add(Job.objects.get(id=jobid))
        client.save()
    return Response({'status': 'success'})
