from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class recetas(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True)
    titulo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, null=True)
    ingredientes = models.TextField()
    detalle = models.TextField()

    def __str__(self):
        return f"{self.categoria} - {self.titulo} | {self.autor}"

