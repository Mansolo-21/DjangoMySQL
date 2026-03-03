from . models import Product
from django import forms

class ProductForm():
    class Meta:
        model = Product
        fields = {'name','description', 'price','image'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms. NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }