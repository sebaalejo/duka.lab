from app.forms import Contacto_form
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
        formulario=Contacto_form(request.POST)
        
        if formulario.is_valid():
            datos=formulario.cleaned_data
            contacto_data=Contacto(nombre=datos['nombre'], apellido=datos["apellido"], email=datos["email"], mensaje=datos["mensaje"])
            contacto_data.save()
            return render(request, "app/inicio.html")




    formulario=Contacto_form()
    contexto={"formulario" : formulario}
    return render(request,  "app/contacto.html", contexto)


def buscar_producto(request):

    return render(request,"app/producto.html")

def resultados_busqueda_producto(request):
    nombre_producto=request.GET["nombre_producto"]

    productos=Producto.objects.filter(nombre__icontains=nombre_producto )
    return render(request, "app/resultados_busqueda_producto.html", {"producto":productos})

def resultados_contacto(request):
    
    contacto=Contacto.objects.all()
    return render(request, "app/resultados_contacto.html", {"contacto":contacto})





    #    nombre_contacto= request.POST["nombre"]
     #   apellido_contacto= request.POST["apellido"]
      #  email_contacto= request.POST["email"]
       # mensaje_contacto=request.POST["mensaje"]

       # contacto= Contacto(nombre= nombre_contacto, apellido=apellido_contacto, email=email_contacto, mensaje=mensaje_contacto )

        #contacto.save()
        #return render(request, "app/inicio.html")

    #return render(request,  "app/contacto.html")