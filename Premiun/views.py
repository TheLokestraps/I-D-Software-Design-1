from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def inicio(request):
   return render(request, "index.html", None)

def conocenos(request):
   return render(request, "about.html", None)


