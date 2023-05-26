# Administración de Pacientes - Consultorio Nutrición

## Instrucciones instalar proyecto en local

- Crea una carpeta contenedora madre
- Abre la consola y ubicate en la carpeta madre
- Crea y activa el ambiente virtual
- Clona este proyecto en la carpeta madre
- Entra en la carpeta que acabas de clonar
- Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
## Usabilidad

### Si se trata de un visitante no registrado/logueado:

    - Recetario:
        - Consultar listado de recetas publicadas.
        - Buscar recetas por categoría
        - Consultar el detalle de cada receta.

    - About: Ver informacion sobre el profesional

    - Iniciar Sesión: Si ya posee una cuenta, puede loguearse en el sistema.

    - Registrarse: Si no posee cuenta, puede crearla desde la plataforma

### Si se trata de un usuario logueado:

    - Recetario:
        - Consultar listado de recetas publicadas.
        - Buscar recetas por categoría
        - Ver el detalle de cada receta.
        - Redactar una nueva receta
        - Acceder a "mis recetas": Lista solo las recetas del usuario, permitiendo:
            - Redactar nueva.
            - Consultar el detalle de una receta.
            - Editar recetas.
            - Eliminar receta.

    - About: Ver informacion sobre el profesional

    - Perfil: En la parte superior derecha muestra un avatar por defecto o la foto de perfil que suba el usuario. Al desplegar el botón se obtiene:
        - Nombre y apellido del usuario.

        - Acceso a Perfil:
            - Muestra y permite editar los datos no sensibles: nombre, apellido y direccón de mail.
            - Muestra la foto de perfil seleccionada. En caso de no tener, habilita un botón para subir su propia imagen.

        - Turnos: En esta sección muestra los turnos solicitados al profesional, permitiendo:
            - Solicitar nuevo turno.
            - Anular turno.

        - Fichas: En esta sección se muestran las fichas de control ingresadas por el usuario, a fin de ir registrando su evolución. Permite:
            - Cargar ficha.
            - Editar datos de una ficha.
            - Eliminar ficha.

        - Mis recetas: es un acceso directo desde el perfil a la seccion mencionada anteriormente.

        - Cerrar sesión: permite desloguear al usuario.    

## Instrucciones para entrar al panel aministrativo de Django

- En consola, crear un superuser:

```
python manage.py createsuperuser
```

- Acceder con user y password via:

```
127.0.0.1:8000/admin
```

# Superusuario de pruebas

```
username:admin
contraseña:admin
```


# Usuarios(pacientes) de pruebas

```
username:01234567892
contraseña:Contra$eña2023

username:01234567891
contraseña:Contra$eña2023

username:01234567890
contraseña:Contra$eña2023
```
