from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from venta.forms import ProductoForm
from .models import Producto
from django.db.models import Q
from django.core.paginator import Paginator

#Create your views here
def para_comprar(request):
    queryset = request.GET.get("buscar")
    productos = Producto.objects.filter()
    if queryset:
        productos = Producto.objects.filter(
            Q(name__icontains = queryset) 
        ).distinct()
    return render (request,"venta/para_comprar.html", {'misProductos': productos})

class ProductoListView(ListView):    
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    #fields = ['name', 'description', 'information', 'image']
    form_class = ProductoForm
    success_url = reverse_lazy('productos')
    def get_success_url(self):
        return reverse_lazy('productos')+'?Creado'

class ProductoUpdate(UpdateView):
    model = Producto
    #fields = ['name', 'description', 'information', 'image']
    form_class = ProductoForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('productos')+'?Actualizado'

class ProductoDelete(DeleteView):
    model = Producto
    def get_success_url(self):
        return reverse_lazy('productos')+'?Eliminado'

class ProductoDetail(DetailView):    
    model = Producto