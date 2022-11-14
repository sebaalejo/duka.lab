from django import forms

class Contacto_form(forms.Form):
    nombre = forms.CharField()
    apellido=forms.CharField()
    email=forms.CharField()
    mensaje=forms.CharField()