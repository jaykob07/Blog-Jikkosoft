from django.shortcuts import render, redirect
from django.views import View 
from django.views.generic import ListView, DetailView
from .models import Articulo, Etiqueta
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView


class Index(ListView):
    model = Articulo
    queyset = Articulo.objects.all().order_by('-fecha')
    template_name = 'blog/index.html'

class DetallesArticulo(DetailView):
    model = Articulo
    template_name = 'blog/blog_post.html'

class UserLogoutView(LogoutView):

    def get(self, request):
        logout(request)
        return redirect('login')

def buscar_por_etiqueta(request, nombre_etiqueta):
    etiqueta = Etiqueta.objects.get(nombre=nombre_etiqueta)
    articulos = Articulo.objects.filter(etiquetas=etiqueta)
    return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'etiqueta': etiqueta})
