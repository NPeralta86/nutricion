from django.urls import path, include
from pacientes.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView

urlpatterns = [
path('registro/', registro, name="registro"),
path('login/', login_view, name="login"),
path('logout/', CustomLogoutView.as_view(), name="logout"),
path('perfil/', MiPerfilUpdateView.as_view(), name="perfil"),
]