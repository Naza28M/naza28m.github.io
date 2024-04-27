from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def compras(request):
    return render(request, "core/compras.html")

def contacto(request):
    return render(request, "core/contacto.html")

def acercade(request):
    return render(request, "core/acercade.html")

def contactar(request):
	if request.method == 'POST':
		asunto = 'Formulario de contacto: ' + request.POST['user_name']
		mensaje = request.POST['message'] +' / Email: '+ request.POST['mail'] + '/ Ciudad: ' + request.POST['ciudad'] + ' / Pais: ' + request.POST['pais'] + ' / Telefono: ' + request.POST['telefono']
		email_desde = settings.EMAIL_HOST_USER
		email_para = ['infopasteleriamvn@gmail.com']
		print('asunto: ', asunto)
		print('mensaje: ', mensaje)
		send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
		return render(request, 'core/contactoExitoso.html')
	return render(request, 'core/contacto.html')
