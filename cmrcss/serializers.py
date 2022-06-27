from rest_framework.serializers import ModelSerializer
from .models import CMRCSS

class CMRCSSCreateSerializer(ModelSerializer):
    class Meta:
        model = CMRCSS
        fields = ['liked', 'feedback']

class CMRCSSSerializer(ModelSerializer):
    class Meta:
        model = CMRCSS
        fields = '__all__'