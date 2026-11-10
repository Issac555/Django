from django.shortcuts import render
from .models import Producto
# Create your views here.

def primera_funcion(request):
    productos = Producto.objects.all()
    
        #ESTRUCTURA
            # if request.method == "POST":
                #EL USUARIO QUIERE EVIAR INFORMACIÓN AL SERVIDOR
            # else: request.method == "GET":
                #Aca requiere informacion
