from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def inicio(request):

   # doc_externo = open("./templates/pixie/index.html")
    #plt = Template(doc_externo.read())
   # doc_externo.close()
    #ctx = Context({})
    #documento = plt.render(ctx)
   return render(request, "index.html", None)

    #return HttpResponse(documento)

