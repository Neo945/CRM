from rest_framework import serializers
from .models import Account, Customer, Customer_Job, Account_Company, Linkedin

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'