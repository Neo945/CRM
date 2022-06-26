from django.forms import CharField, ModelForm
from .models import CMRCSS

DEPARTMENT_CHOICES = (
    ('MRK','Marketing'),
    ('OPR','Opetration'),
    ('SLS','Sales'),
    ('PSLS','PreSales'),
)

class CMRCSSForm(ModelForm):
    # department = CharField(max_length=100, choice=DEPARTMENT_CHOICES, required=True)
    class Meta:
        model = CMRCSS
        # fields = ['liked', 'feedback', 'customer', 'department']
        fields = ['liked', 'feedback']