from email.message import EmailMessage
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import Company, Job, Profile
from accounts.serializers import CompanySerializer, JobCreateSerializer, JobSerializer, ProfileCreateSerializer, ProfileSerializer, UserSerializer
from django.db.models import Q

# tested
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_company(request):
    if request.user.is_authenticated and request.user.is_superuser:
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Company created successfully", "sucess": True, "data": serializer.data}, status=201)
        return Response({"message":"Company not created", "sucess": False}, status=400)
    return Response({"message":"User is not authenticated", "sucess": False}, status=400)

@api_view(['GET'])
def get_company(request, company_id):
    company = Company.objects.filter(id=company_id)
    if company.exists():
        return Response({"message":"Company created successfully", "sucess": True, "company": CompanySerializer(company.first()).data}, status=200)
    return Response({"message":"Company Not found", "sucess": False}, status=404)


@api_view(['POST'])
def reg_view(request):
    """
    {
        "email": "shreesh@gmail.com",
        "password1": "$#p7j!<{L9P3j-1",
        "password2": "$#p7j!<{L9P3j-1",
        "username": "shree1",
        "csrftoken": "oql2VrzNNrZy7q9blHdipSoi3s4Tenpb2osmfxmmwJyD9aoWRxx86ob4O6z6sWje"
    }    
    """
    form = UserCreationForm(request.data or None)
    serializer = ProfileCreateSerializer(data=request.data)
    if form.is_valid() and serializer.is_valid():
        user = form.save(commit=True)
        profile = serializer.save(user=user)
        return Response({"message":"Register Successful", "sucess": True, "user": ProfileSerializer(profile).data}, status=201)
    return Response({"message":"Register Failed", "sucess": False}, status=400)


@api_view(['POST'])
def login_view(request):
    """
    {
        "email": "shreesh@gmail.com",
        "password": "$#p7j!<{L9P3j-1",
        "username": "shree1"
    }
    """
    if not request.user.is_authenticated:
        form = AuthenticationForm(request,data=request.data)
        if form.is_valid():
            user_ = form.get_user()
            login(request,user_)
            return Response({"message":"Login Successful", "sucess": True, "user": ProfileSerializer(Profile.objects.get(user=user_)).data}, status=201)
        return Response({"message":"Login Failed", "sucess": False}, status=400)
    return Response({"message":"Already logged in", "sucess": False}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_password(request):
    """
    {
        "old_password": "$#p7j!<{L9P3j-1",
        "new_password1": "$#p7j!<{L9P3j-1",
        "new_password2": "$#p7j!<{L9P3j-1",
        "csrftoken": "oql2VrzNNrZy7q9blHdipSoi3s4Tenpb2osmfxmmwJyD9aoWRxx86ob4O6z6sWje"
    }
    """
    if request.user.is_authenticated:
        form = AuthenticationForm(request,data=request.data)
        if form.is_valid():
            user_ = form.get_user()
            user_.set_password(request.data['new_password1'])
            user_.save()
            return Response({"message":"Password Updated", "sucess": True, "user": ProfileSerializer(Profile.objects.get(user=user_)).data}, status=201)
        return Response({"message":"Password Update Failed", "sucess": False}, status=400)
    return Response({"message":"User is not authenticated", "sucess": False}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message":"Logout Successful", "sucess": True}, status=200)

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.user.is_authenticated:
        return Response({'message': "user is authenticated", "success": True, 'user': ProfileSerializer(Profile.objects.get(user=request.user)).data})
    return Response({'message': "user is not authenticated","success": False})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_jobs(request):
    serializer = JobCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = Profile.objects.get(user=request.user)
        instance = serializer.save(company=user.company, created_by=user)
        return Response({"message":"Job created successfully", "sucess": True, "data": JobSerializer(instance).data}, status=201)
    return Response({"message":"Job not created", "sucess": False}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_jobs(request, job_id):
    if request.user.is_authenticated:
        return Response({"message":"Job created successfully", "sucess": True, "job": JobSerializer(Job.objects.get(id=job_id)).data}, status=201)
    return Response({"message":"User is not authenticated", "sucess": False}, status=400)


@api_view(['POST'])
def send_email_data(request):
    subject = request.data['subject']
    message = '<h1>' + request.data['message'] + '</h1>'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.data['email']]
    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
    file = request.FILES['file']
    mail.attach(file.name, file.read(), file.content_type)
    if mail.send():
        return Response({"message":"Email sent successfully", "sucess": True}, status=200)
    return Response({"message":"Email not sent", "sucess": False}, status=400)

@api_view(['GET'])
def search_company(request):
    return Response({"sucess": True, "company": CompanySerializer(Company.objects.filter(Q(name__icontains=request.query_params['str']) | Q(address__icontains=request.query_params['str']))).data})


@api_view(['GET'])
def search_job(request):
    return Response({"sucess": True, "company": JobSerializer(Job.objects.filter(Q(name__icontains=request.query_params['str']) | Q(requirements__icontains=request.query_params['str']))).data})
