from django.shortcuts import render
from login.models import Cliente
import pathlib
# Create your views here.

#variables
location = pathlib.Path().resolve()



#views
def login(request):

    correo   = request.GET.get("email")
    password = request.GET.get("password")

    usuarios  = Cliente.objects.filter(email=correo).filter(password=password)
    

    return render(request, "{}/login/templates/login.html".format(location))

def registry(request):
    return render(request,"{}/login/templates/registry.html".format(location))

def session(request):

    nombre   = request.GET.get("nombre")
    apellido = request.GET.get("apellido")
    correo   = request.GET.get("email")
    password = request.GET.get("password")

    return render(request,"{}/Premiun/login/templates/session.html".format(location))

