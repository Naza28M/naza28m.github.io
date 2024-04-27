from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['name', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre':'','precio': '', 'descripcion':'',  'imagen': ''
        }