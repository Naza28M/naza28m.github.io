from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from libreta.forms import RecetaForm
from .models import Receta
from django.db.models import Q
from django.core.paginator import Paginator

#Create your views here
def para_recetas(request):
    recetas = Receta.objects.all()
    return render (request,"libreta/para_recetas.html", {'misRecetas': recetas})

#barra para buscador
def para_recetas(request):
    queryset = request.GET.get("buscar")
    recetas = Receta.objects.filter()
    if queryset:
        recetas = Receta.objects.filter(
            Q(name__icontains = queryset) 
        ).distinct()
    return render (request,"libreta/para_recetas.html", {'misRecetas': recetas})
    
class RecetaListView(ListView):    
    model = Receta

class RecetaCreate(CreateView):
    model = Receta
    #fields = ['name', 'description', 'information', 'image']
    form_class = RecetaForm
    success_url = reverse_lazy('recetas')
    def get_success_url(self):
        return reverse_lazy('recetas')+'?Creado'

class RecetaUpdate(UpdateView):
    model = Receta
    #fields = ['name', 'description', 'information', 'image']
    form_class = RecetaForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('recetas')+'?Actualizado'

class RecetaDelete(DeleteView):
    model = Receta
    def get_success_url(self):
        return reverse_lazy('recetas')+'?Eliminado'

class RecetaDetail(DetailView):    
    model = Receta