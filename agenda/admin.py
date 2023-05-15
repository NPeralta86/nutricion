from django.contrib import admin
from .models import pacientes, agenda, ficha

# Register your models here.
admin.site.register(pacientes)
admin.site.register(agenda)
admin.site.register(ficha)
