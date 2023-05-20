from django.urls import path, include
from pacientes.views import registro

urlpatterns = [
path('registro/', registro, name="registro"),
]