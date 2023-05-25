from django import forms

class form_recetas(forms.Form):
    titulo = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Título','class':'form-control'}))
    categoria = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Categoría','class':'form-control'}))
    ingredientes = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Ingredientes','class':'form-control'}))
    detalle = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Preparación','class':'form-control'}))
    
    
