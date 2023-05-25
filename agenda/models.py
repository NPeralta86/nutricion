from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class pacientes(models.Model):
    cuil = models.CharField(max_length=11, primary_key=True)
    apellido = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    nacimiento = models.DateField(null=True)

    tipos_generos = [("M", "Masculino"), ("F", "Femenino"), ("X", "No binario / No responde")]
    genero=models.CharField(max_length=1, choices=tipos_generos)

    def __str__(self):
        return f"{self.apellido}, {self.nombres} | CUIL: {self.cuil} "


class agenda(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha=models.DateField(null=True)
    hora=models.TimeField(null=True)
    descripcion=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.hora} | {self.paciente}"


class ficha(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True)
    peso=models.FloatField(null=True)
    talla=models.FloatField(null=True)
    imc=models.FloatField(null=True)
    observaciones=models.CharField(max_length=1000, blank=True)

    def imc(self):
        self.imc = self.peso / (self.talla ** 2)

    def __str__(self):
        return f"{self.paciente} - {self.fecha} "
