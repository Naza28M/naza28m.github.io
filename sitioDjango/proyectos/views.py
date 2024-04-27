from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from proyectos.forms import ProyectoForm
from django.db.models import Q
from .models import Proyecto

#Create your views here

def trabajos(request):
    proyectos = Proyecto.objects.all()
    return render (request, "proyectos/proyecto_list.html", {'proyecto_list': proyectos})

# Create your views here.
class ProyectoListView(ListView):    
    model = Proyecto

class ProyectoCreate(CreateView):
    model = Proyecto
    #fields = ['name', 'description', 'image', 'webside']
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos')
    def get_success_url(self):
        return reverse_lazy('proyectos')+'?Creado'

class ProyectoUpdate(UpdateView):
    model = Proyecto
    #fields = ['name', 'description', 'image', 'webside']
    form_class = ProyectoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('proyectos')+'?Actualizado'

class ProyectoDelete(DeleteView):
    model = Proyecto
    def get_success_url(self):
        return reverse_lazy('proyectos')+'?Eliminado'

class ProyectoDetail(DetailView):    
    model = Proyecto