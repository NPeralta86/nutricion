
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from pacientes.forms import UserRegisterForm, UserLoginForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('index')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='pacientes/registro.html',
       context={'form': formulario},
   )


def login_view(request):
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               url_exitosa = reverse('index')
               return redirect(url_exitosa)
   else:  # GET
       form = UserLoginForm()
   return render(
       request=request,
       template_name='pacientes/login.html',
       context={'form': form},
   )


class CustomLogoutView(LogoutView):
   template_name = 'agenda/index.html'
