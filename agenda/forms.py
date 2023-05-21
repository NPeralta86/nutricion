from django import forms

class form_pacientes(forms.Form):
    cuil = forms.CharField(required=True, max_length=11, label='', widget=forms.TextInput(attrs={'placeholder': 'Cuil','class':'form-control'}))
    apellido = forms.CharField(required=True, max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Apellido','class':'form-control'}))
    nombres = forms.CharField(required=True, max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Nombres','class':'form-control'}))
    nacimiento = forms.DateField(label='', widget=forms.TextInput(attrs={'placeholder': 'Fecha de Nacimiento','class':'form-control'}))
    genero = forms.CharField(max_length=1, label='', widget=forms.TextInput(attrs={'placeholder': 'Género','class':'form-control'}))

class form_agenda(forms.Form):
    # paciente = forms.CharField(required=True, max_length=11, label='', widget=forms.TextInput(attrs={'placeholder': 'Cuil','class':'form-control'}))
    fecha = forms.DateField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Fecha turno','class':'form-control'}))
    hora = forms.TimeField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Hora turno','class':'form-control'}))
    descripcion = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Notas','class':'form-control'}))

class form_ficha(forms.Form):
    paciente = forms.CharField(required=True, max_length=11, label='', widget=forms.TextInput(attrs={'placeholder': 'Cuil','class':'form-control'}))
    fecha = forms.DateField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Fecha control','class':'form-control'}))
    peso = forms.FloatField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Peso (kg)','class':'form-control'}))
    talla = forms.FloatField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Talla (m)','class':'form-control'}))
    observaciones = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'placeholder': 'Notas','class':'form-control'}))
