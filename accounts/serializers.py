from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Company, Job, Profile

class CompanySerializer(serializers.ModelSerializer):
    job = serializers.SerializerMethodField('get_jobs')

    def get_jobs(self, obj):
        return JobSerializer(Job.objects.filter(company=obj), many=True).data
    


    class Meta:
        model = Company
        fields = ('name','address','phone','email','website','job')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)

class ProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('user','type', 'company', 'email', 'first_name', 'last_name')

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('type', 'company', 'email', 'first_name', 'last_name')

class JobSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(read_only=True)
    # created_by = ProfileSerializer(read_only=True)
    class Meta:
        model = Job
        fields = ('name','description','linkedin_url','requirements','image', 'created_by')


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name','description','linkedin_url','requirements' ,'image','document')