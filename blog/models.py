from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = HTMLField(default="Sin contenido")
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    etiqueta = models.ManyToManyField(Etiqueta, blank=True)


    
