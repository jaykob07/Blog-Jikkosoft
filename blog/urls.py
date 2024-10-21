from django.urls import path,include    
from .views import Index,  buscar_por_etiqueta, DetallesArticulo 


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('buscar/<str:nombre_etiqueta>/', buscar_por_etiqueta, name='buscar_por_etiqueta'),
    path('<int:pk>/', DetallesArticulo.as_view(), name='detalle_articulo'),
]