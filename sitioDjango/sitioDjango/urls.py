"""sitioDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views
from proyectos import views as proyectos_views
from venta import views as venta_views
1#from recetas import views as recetas_views
from proyectos.views import (ProyectoCreate, ProyectoDelete, ProyectoListView, ProyectoUpdate, ProyectoDetail)
from libreta import views as libreta_views
from libreta.views import (RecetaCreate, RecetaDelete, RecetaUpdate, RecetaDetail)
from venta.views import (ProductoCreate, ProductoDelete, ProductoUpdate, ProductoDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('acercade/', views.acercade, name='acercade'),
    path('compras/', views.compras, name='compras'),

    path('listProyectos/', ProyectoListView.as_view(),name='proyectos'),
    path('create/', ProyectoCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProyectoUpdate.as_view(), name='update'),		
    path('delete/<int:pk>/', ProyectoDelete.as_view(), name='delete'),	
    path('detail/<int:pk>/', ProyectoDetail.as_view(), name='detail'),

	path ('para_recetas/', libreta_views.para_recetas,name='recetas'),
    path('createR/', RecetaCreate.as_view(), name='createR'),
    path('rupdate/<int:pk>/', RecetaUpdate.as_view(), name='rupdate'),		
    path('rdelete/<int:pk>/', RecetaDelete.as_view(), name='rdelete'),	
    path('rdetail/<int:pk>/', RecetaDetail.as_view(), name='rdetail'),

    path ('para_comprar/', venta_views.para_comprar,name='productos'),
    path('createP/', ProductoCreate.as_view(), name='createP'),
    path('Pupdate/<int:pk>/', ProductoUpdate.as_view(), name='Pupdate'),		
    path('Pdelete/<int:pk>/', ProductoDelete.as_view(), name='Pdelete'),	
    path('Pdetail/<int:pk>/', ProductoDetail.as_view(), name='Pdetail'),

    path('contactar/', views.contactar),
]

#Configuracion extendida para mostrar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)