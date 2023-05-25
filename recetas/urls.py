from django.urls import path, include
from . import views

#from recetas.views import 

urlpatterns = [
    path('recetas/', views.vista_recetas, name="recetas"),
    path('recetas-agregar/', views.vista_recetas_agregar, name="recetas_agregar"),
    path('recetas-detalle/<int:pk>/', views.vista_recetas_detalle, name="recetas_detalle"),
    path('recetas-buscar/', views.vista_recetas_buscar, name="recetas_buscar"),
    path('recetas-editar/<int:pk>/', views.vista_recetas_editar, name="recetas_editar"),
    path('recetas-eliminar/<int:pk>/', views.vista_recetas_eliminar, name="recetas_eliminar"),

]
