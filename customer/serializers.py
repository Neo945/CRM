from rest_framework import serializers

from accounts.serializers import JobSerializer
from .models import Client, Customer, Customer_Job, Linkedin

class LinkedinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linkedin
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True, read_only=True)
    linkedin = LinkedinSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email', 'website', 'description', 'date_created', 'date_updated', 'linkedin', 'job')

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email', 'website', 'description')

