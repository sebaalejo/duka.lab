from app.forms import Contacto
from app.models import *
from django.shortcuts import render
from django.template import Context, Template

# Create your views here.


def inicio(request):
    return render(request,  "app/inicio.html")

def producto(request):
    return render(request,  "app/producto.html")

def about(request):
    return render(request,  "app/about.html")

def contacto(request):

    if request.method=="POST":
        formulario=Contacto(request.POST)
        
        if formulario.is_valid():
            data=formulario.cleaned_data
            contacto=Contacto(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], mensaje=data["mensaje"])
            contacto.save()
        return render(request, "app/inicio.html")

    else:
        formulario=Contacto()

    contexto={"formulario":formulario}
    return render(request,  "app/contacto.html", contexto)









    #    nombre_contacto= request.POST["nombre"]
     #   apellido_contacto= request.POST["apellido"]
      #  email_contacto= request.POST["email"]
       # mensaje_contacto=request.POST["mensaje"]

       # contacto= Contacto(nombre= nombre_contacto, apellido=apellido_contacto, email=email_contacto, mensaje=mensaje_contacto )

        #contacto.save()
        #return render(request, "app/inicio.html")

    #return render(request,  "app/contacto.html")