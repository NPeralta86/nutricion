from django.shortcuts import render, redirect
from django.urls import reverse

from .models import agenda, pacientes, ficha
from .forms import form_pacientes, form_agenda, form_ficha
# Create your views here.


def vista_pacientes(request):
    contexto = {
        "pacientes": pacientes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='agenda/pacientes.html',
        context=contexto,
    )
    return http_response


def vista_pacientes_agregar(request):
    if request.method == "POST":
        formulario = form_pacientes(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cuil = data["cuil"]
            apellido = data["apellido"]
            nombres = data["nombres"]
            nacimiento = data["nacimiento"]
            genero = data["genero"]

            paciente = pacientes(cuil=cuil, apellido=apellido,
                                 nombres=nombres, nacimiento=nacimiento, genero=genero)
            paciente.save()

            url_exitosa = reverse('pacientes')
            return redirect(url_exitosa)

    else:
        formulario = form_pacientes()
        contexto = {'formulario': formulario}
        http_response = render(
            request=request,
            template_name='agenda/pacientes_agregar.html',
            context=contexto,
        )
        return http_response


def vista_pacientes_eliminar(request, id):
    paciente = pacientes.objects.get(cuil=id)
    if request.method == "POST":
        paciente.delete()
        url_exitosa = reverse('pacientes')
        return redirect(url_exitosa)


def vista_pacientes_buscar(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        paciente = pacientes.objects.filter(apellido__icontains=busqueda)
        contexto = {
            "pacientes": paciente,
        }
        http_response = render(
            request=request,
            template_name='agenda/pacientes.html',
            context=contexto,
        )
        return http_response


def vista_agenda(request):
    contexto = {
        "agenda": agenda.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='agenda/agenda.html',
        context=contexto,
    )
    return http_response


def vista_agenda_agregar(request):
    if request.method == "POST":
        formulario = form_agenda(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente = data["paciente"]
            fecha = data["fecha"]
            hora = data["hora"]
            descripcion = data["descripcion"]

            turno = agenda(paciente=paciente, fecha=fecha,
                               hora=hora, descripcion=descripcion)
            turno.save()

            url_exitosa = reverse('agenda')
            return redirect(url_exitosa)

    else:
        formulario = form_agenda()
        contexto = {'formulario': formulario}
        http_response = render(
            request=request,
            template_name='agenda/agenda_agregar.html',
            context=contexto,
        )
        return http_response


def vista_ficha(request):
    contexto = {
        "ficha": ficha.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='agenda/ficha.html',
        context=contexto,
    )
    return http_response


def vista_ficha_agregar(request):
    if request.method == "POST":
        formulario = form_ficha(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente = data["paciente"]
            fecha = data["fecha"]
            peso = data["peso"]
            talla = data["talla"]
            observaciones = data["observaciones"]

            control = ficha(paciente=paciente, fecha=fecha,
                           peso=peso, talla=talla, observaciones=observaciones)
            control.save()

            url_exitosa = reverse('ficha')
            return redirect(url_exitosa)

    else:
        formulario = form_ficha()
        contexto = {'formulario': formulario}
        http_response = render(
            request=request,
            template_name='agenda/ficha_agregar.html',
            context=contexto,
        )
        return http_response