from django.shortcuts import render
from rest_framework.response import Response
from django.conf import settings
from cryptography.fernet import Fernet
import json

from cmrcss.forms import CMRCSSForm
from cmrcss.serializers import CMRCSSCreateSerializer, CMRCSSSerializer
from leads.models import MarketingLead, OperationLead, PreSalesLead, SalesLead
from rest_framework.decorators import api_view

@api_view(['POST'])
def index(request, token):
    print(request.data)
    serializer = CMRCSSCreateSerializer(data=request.data)
    if serializer.is_valid():
        fernet = Fernet(settings.KEY)
        data = json.loads(fernet.decrypt(token.encode()).decode())
        print(data)
        cmr = serializer.save()
        if data['status'] == 'MRK':
            lead = MarketingLead.objects.get(id=data['id'])
            lead.cmrcss = cmr
            lead.save()
        elif data['status'] == 'OPR':
            lead = OperationLead.objects.get(id=data['id'])
            lead.cmrcss = cmr
            lead.save()
        elif data['status'] == 'SLS':
            lead = SalesLead.objects.get(id=data['id'])
            lead.cmrcss = cmr
            lead.save()
        elif data['status'] == 'PSLS':
            lead = PreSalesLead.objects.get(id=data['id'])
            lead.cmrcss = cmr
            lead.save()
        return Response({'status': 'success', 'message': CMRCSSSerializer(cmr).data})
    return Response({'status': 'error'})

