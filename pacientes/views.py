
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from pacientes.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, AvatarFormulario
#from pacientes.models import Avatar

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView




def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('login')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='pacientes/registro.html',
       context={'form': formulario},
   )


def login_view(request):
   next_url = request.GET.get('next')
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
               if next_url:
                return redirect(next_url)
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


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('perfil')
   template_name = 'pacientes/perfil.html'

   def get_object(self, queryset=None):
       return self.request.user


def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarFormulario(request.POST, request.FILES)

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('perfil')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarFormulario()
  return render(
      request=request,
      template_name="pacientes/perfil_avatar.html",
      context={'form': formulario},
  )
