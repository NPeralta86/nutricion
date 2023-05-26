from django.urls import path
from . import views

urlpatterns = [
    # path('pacientes/', views.vista_pacientes, name="pacientes"),
    # path('pacientes-agregar/', views.vista_pacientes_agregar, name="pacientes_agregar"),
    # path('pacientes-editar/<int:pk>/', views.vista_pacientes_editar, name="pacientes_editar"),
    # path('pacientes-eliminar/<int:pk>/', views.vista_pacientes_eliminar, name="pacientes_eliminar"),
    # path('pacientes-buscar/', views.vista_pacientes_buscar, name="pacientes_buscar"),
    
    path('agenda/', views.vista_agenda, name="agenda"),
    path('agenda-agregar/', views.vista_agenda_agregar, name="agenda_agregar"),
    path('agenda-eliminar/<int:pk>/', views.vista_agenda_eliminar, name="agenda_eliminar"),

    path('ficha/', views.vista_ficha, name="ficha"),
    path('ficha-agregar/', views.vista_ficha_agregar, name="ficha_agregar"),
    path('ficha-editar/<int:pk>/', views.vista_ficha_editar, name="ficha_editar"),
    path('ficha-eliminar/<int:pk>/', views.vista_ficha_eliminar, name="ficha_eliminar"),
]

