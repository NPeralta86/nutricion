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

Mediante la barra de navegación se puede acceder a:

    - Modulo Pacientes:
        - Consultar listado de pacientes.
        - Agregar nuevo paciente.
        - Buscar paciente dentro del listado, por apellido. Tipo de búsqueda: icontains (coincidencia, no palabras exactas).
    
    - Módulo Agenda:
        - Consultar listado de turnos.
        - Solicitar / Cargar un nuevo turno.

    - Módulo Fichas:
        - Consultar listado fichas de seguimiento.
        - Cargar un nueva ficha de control.

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
