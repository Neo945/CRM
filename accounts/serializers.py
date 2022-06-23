from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name','address','phone','email','website',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class ProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('user','type', 'company',)