from django.forms import ModelForm, TextInput, Textarea
from .models import Category


class CategoriesForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'name': 'Category'
        }
