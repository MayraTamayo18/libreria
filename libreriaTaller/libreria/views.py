from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializer import libroSerializer
from .models import libro

from .serializer import usuarioSerializer
from .models import usuario

from .serializer import prestamoSerializer
from .models import prestamo

from .serializer import multaSerializer
from .models import multa

# Create your views here.

#se crea la clase view por cada modelo
class libroView(viewsets.ModelViewSet):
    serializer_class=libroSerializer
    queryset=libro.objects.all()
    #para filtro de buscar 
    filter_backends=[filters.SearchFilter]
    search_fields=['$titulo', '$autor', '$genero', '$isbn']
    
class usuarioView(viewsets.ModelViewSet):
    serializer_class=usuarioSerializer
    queryset=usuario.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields=['$nombre', '$correo']
    
class prestamoView(viewsets.ModelViewSet):
    serializer_class=prestamoSerializer
    queryset=prestamo.objects.all()

class multaView(viewsets.ModelViewSet):
    serializer_class=multaSerializer
    queryset=multa.objects.all()