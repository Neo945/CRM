from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    if request.user.is_authenticated:
        return Response({'message': "user is authenticated", "success": True, 'user': UserSerializer(request.user).data})
    return Response({'message': "user is not authenticated","success": False})

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
            return Response({"message":"Login Successful", "sucess": True, "user": UserSerializer(user_).data}, status=201)
        return Response({"message":"Login Failed", "sucess": False}, status=400)
    return Response({"message":"Already logged in", "sucess": False}, status=400)

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
    if form.is_valid():
        user = form.save(commit=True)
        return Response({"message":"Register Successful", "sucess": True, "user": UserSerializer(user).data}, status=201)
    return Response({"message":"Register Failed", "sucess": False}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"message":"Logout Successful", "sucess": True}, status=200)
