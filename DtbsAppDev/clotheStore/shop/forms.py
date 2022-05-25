from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'image', 'description', 'price', 'available','percent','spring/summer','fall/winter')

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ImageField(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'percent': forms.DurationField(attrs={'class': 'form-control'}),
            'spring/summer': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'fall/winter': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }