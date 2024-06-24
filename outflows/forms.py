from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, NumberInput, Textarea
from .models import Outflow

class OutflowForm(ModelForm):
    
    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': Select(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        
        if quantity > product.quantity:
            raise ValidationError(
                f'The available stock quantity for the product {product.title} is {product.quantity} units.')
        
        return quantity
