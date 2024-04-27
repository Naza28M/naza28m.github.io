from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['name', 'description', 'information', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'information': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre':'', 'descripcion':'', 'informacion': '', 'imagen': ''
        }
