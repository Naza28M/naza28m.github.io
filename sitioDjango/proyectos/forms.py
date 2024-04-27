from django import forms

from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['name', 'description', 'image', 'webside']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre':'', 'descripcion':'', 'imagen': '', 'url': ''
        }
