from django.forms import ModelForm, TextInput, Textarea
from .models import Brand


class BrandForm(ModelForm):
    
    class Meta:
        model = Brand
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'name': 'Brand',
        }