from django.urls import path
from app import views


urlpatterns = [
    path("inicio/", views.inicio, name= "Inicio"),
    path("producto/", views.producto, name="Producto"),
    path("about/", views.about, name="About"),
    path("contacto/", views.contacto, name="Contacto_url"),
    path("producto/", views.buscar_producto, name="buscar_producto"),
    path("producto/resultados", views.resultados_busqueda_producto, name="resultado_busqueda_producto"),
    path("contacto/resultados", views.resultados_contacto, name="resultados_contacto"),
]