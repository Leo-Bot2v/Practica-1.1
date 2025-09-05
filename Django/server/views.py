from django.shortcuts import render

# Create your views here.

def inicio(request, seccion=None):
    if seccion not in ["habilidades", "experiencia", "contacto"]:
        seccion = "habilidades"  # por defecto
    return render(request, "index.html", {"seccion": seccion})