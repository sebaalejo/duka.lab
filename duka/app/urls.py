from django.urls import path
from app import views


urlpatterns = [
    path("inicio/", views.inicio, name= "Inicio"),
    path("producto/", views.producto, name="Producto"),
    path("about/", views.about, name="About"),
    path("contacto/", views.contacto, name="Contacto")

]