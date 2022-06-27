from rest_framework import serializers
from django.contrib.auth.models import User
from customer.models import Client
from cmrcss.serializers import CMRCSSSerializer

from customer.serializers import CustomerSerializer, LinkedinSerializer
from accounts.serializers import JobSerializer, ProfileSerializer
from .models import Leads, MarketingLead, OperationLead, PreSalesLead, SalesLead

class LeadsSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Leads
        fields = ('is_done','id', 'customer', 'date_updated', 'date_created')

class MarketingSerializer(serializers.ModelSerializer):
    leads = LeadsSerializer(read_only=True)
    approved_by = ProfileSerializer(read_only=True)
    cmrcss = CMRCSSSerializer(read_only=True)
    class Meta:
        model = MarketingLead
        fields = ('id','is_done','leads','approved_by','date_created','date_updated','refered_by_name','refered_source','requirements','cmrcss')


class MarketingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingLead
        fields = ('refered_by_name','refered_source','requirements')


class SalesSerializer(serializers.ModelSerializer):
    marketinglead = MarketingSerializer(read_only=True)
    approved_by = ProfileSerializer(read_only=True)
    cmrcss = CMRCSSSerializer(read_only=True)
    class Meta:
        model = SalesLead
        fields = ('id','is_done','approved_by','marketinglead','date_created','date_updated','sales_details','sales_pricing','cmrcss')

class SalesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesLead
        fields = ('sales_details','sales_pricing')


class PreSalesSerializer(serializers.ModelSerializer):
    cmrcss = CMRCSSSerializer(read_only=True)
    saleslead = SalesSerializer(read_only=True)
    approved_by = ProfileSerializer(read_only=True)
    class Meta:
        model = PreSalesLead
        fields = ('id','is_done','approved_by', 'saleslead','date_created','date_updated', 'proposal_details','proposal_date','cmrcss')


class PreSalesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSalesLead
        fields = ( 'proposal_details','proposal_date')

class OperationSerializer(serializers.ModelSerializer):
    cmrcss = CMRCSSSerializer(read_only=True)
    presaleslead = PreSalesSerializer(read_only=True)
    approved_by = ProfileSerializer(read_only=True)
    class Meta:
        model = OperationLead
        fields = ('id','is_done','presaleslead','approved_by','date_created','date_updated','cmrcss')

class OperationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLead
        fields = ('deal_details',"deal_status",'detail_pricing')

class ClientSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True, read_only=True)
    linkedin = LinkedinSerializer(read_only=True)
    operations = OperationSerializer(read_only=True)

    class Meta:
        model = Client

        fields = ('id', 'operations', 'name', 'phone', 'email', 'website', 'address','description', 'date_created', 'date_updated', 'linkedin', 'job')
