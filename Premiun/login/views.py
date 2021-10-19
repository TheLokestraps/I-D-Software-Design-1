from django.shortcuts import render
from login.models import Cliente
import pathlib
# Create your views here.

#variables
location = pathlib.Path().resolve()



#views
def login(request):

    correo   = request.GET["email"]
    password = request.GET["password"]

    usuarios  = Cliente.objects.filter(email=correo).filter(password=password)
    

    return render(request, "{}/Premiun/login/templates/login.html".format(location)) 

def registry(request):
    return render(request,"{}/Premiun/login/templates/registry.html".format(location))

def session(request):

    nombre   = request.GET["nombre"]
    apellido = reques.GET["apellido"]
    correo   = request.GET["email"]
    password = request.GET["password"]

    return render(request,"{}/Premiun/login/templates/session.html".format(location))