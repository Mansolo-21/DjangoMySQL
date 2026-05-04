from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

from django import forms

class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(
        max_length=12, min_length=12,
        widget=forms.TextInput(attrs={
            'placeholder': '2547XXXXXXXX',
            'class': 'form-control',
            'pattern': '2547\d{8}',
            'title': 'Enter a valid Kenyan number'
        })
    )
    amount = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter Amount',
            'class': 'form-control'
        })
    )