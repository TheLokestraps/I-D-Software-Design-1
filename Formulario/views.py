from django.shortcuts import render
from .models import Formulario
import json

def inicio(request):
   return render(request, "index.html", None)

def conocenos(request):
   return render(request, "about.html", None)

def ofrecer(request):
   return render(request, "contact.html", None)

def aviso(request):
  #print(request.POST["Nombre"], request.POST["Email"], request.POST["Indicativo"], request.POST["Telefono"], request.POST["DocumentoIdentidad"])
   x = Formulario(nombreCompleto=request.POST["Nombre"], email=request.POST["Email"], indicativo= request.POST["Indicativo"], telefono= request.POST["Telefono"], docIdentidad= request.POST["DocumentoIdentidad"])
   x.save()
   mensaje = request.POST["Nombre"]
   return render(request, "aviso.html", {"mensaje": mensaje})