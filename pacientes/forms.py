from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
   # Esto es un ModelForm
   username = forms.CharField(label='', max_length=11,widget=forms.TextInput(attrs={'placeholder': 'Cuil - sin guiones-', 'class ': 'form-control'}))
   last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class ':'form-control'}))
   first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombres', 'class ': 'form-control'}))
   birth_date = forms.DateField(label='', widget=forms.DateInput(
       attrs={'placeholder': 'Fecha de nacimiento', 'class ': 'form-control'}))
   gender = forms.CharField(label='', max_length=1, widget=forms.TextInput(
       attrs={'placeholder': 'Género', 'class ': 'form-control'}))
   email = forms.EmailField(label='', widget=forms.EmailInput(
       attrs={'placeholder': 'E-mail', 'class ': 'form-control'}))
   password1 = forms.CharField(label='', widget=forms.PasswordInput(
       attrs={'placeholder': 'Contraseña', 'class ': 'form-control'}))
   password2 = forms.CharField(label='', widget=forms.PasswordInput(
       attrs={'placeholder': 'Repetir Contraseña', 'class ': 'form-control'}))

   class Meta:
       model = User
       fields = ['username', 'last_name', 'first_name', 'birth_date', 'gender',
                 'email', 'password1', 'password2']
