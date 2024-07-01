from django.forms import ModelForm, TextInput, Select, Textarea, CharField
import re
from typing import Any
from .models import Product


class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['title', 'brand', 'category', 'description',
                  'serie_number', 'cost_price', 'selling_price']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'brand': Select(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'serie_number': TextInput(attrs={'class': 'form-control'}),
            'cost_price': TextInput(attrs={'class': 'form-control'}),
            'selling_price': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Product Name',
            'cost_price': 'Cost Price',
            'selling_price': 'Selling Price',
        }
