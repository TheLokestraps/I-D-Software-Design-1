from django.shortcuts import render
import pathlib
# Create your views here.

#variables
location = pathlib.Path().resolve()



#views
def login(request):

    return render(request, "{}/Premiun/login/templates/login.html".format(location)) 
   


def registry(request):
    return render(request,"{}/Premiun/login/templates/registry.html".format(registry))