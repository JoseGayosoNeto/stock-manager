from django.forms import ModelForm, Select, NumberInput, Textarea
from .models import Inflow


class InflowForm(ModelForm):
    
    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': Select(attrs={'class':'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
