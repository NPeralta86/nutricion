from django.contrib.auth.models import User
from django.test import TestCase
from .models import recetas

class RecetaTest(TestCase):

    def setUp(self):
        # Crear un usuario "Prueba" para utilizar como autor
        self.user = User.objects.create_user(
            username='Prueba', password='Prueba')

    def test_creacion_receta(self):
        receta = recetas(autor=self.user, fecha="2001-01-01", titulo="Titulo prueba",
                         categoria="Categoria prueba", ingredientes="Ingredientes prueba", detalle="Detalle prueba")
        receta.save()

        self.assertEqual(recetas.objects.count(), 1)
        # Comprobar que el autor es el usuario "Prueba"
        self.assertEqual(receta.autor, self.user)
        # Resto de las aserciones...

    def test_receta_str(self):
        receta = recetas(autor=self.user, fecha="2001-01-01", titulo="Titulo prueba",
                         categoria="Categoria prueba", ingredientes="Ingredientes prueba", detalle="Detalle prueba")
        receta.save()

        self.assertEqual(receta.__str__(),
                         "Categoria prueba - Titulo prueba | Prueba")
