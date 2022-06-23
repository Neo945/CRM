from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Marketing, Sales, PreSales, Operation

class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class PreSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSales
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'