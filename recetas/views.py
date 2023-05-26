from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import recetas
from .forms import form_recetas


# Create your views here.


def vista_recetas(request):
    contexto = {
        "recetas": recetas.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='recetas/recetas.html',
        context=contexto,
    )
    return http_response

@login_required
def vista_recetas_autor(request):
    contexto = {
        "recetas": recetas.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='recetas/recetas_autor.html',
        context=contexto,
    )
    return http_response


@login_required
def vista_recetas_agregar(request):
    if request.method == "POST":
        formulario = form_recetas(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autor = request.user
            fecha = datetime.now().date()
            titulo = data["titulo"]
            categoria = data["categoria"]
            ingredientes = data["ingredientes"]
            detalle = data["detalle"]

            receta = recetas(autor=autor, fecha=fecha, titulo=titulo,
                             categoria=categoria, ingredientes=ingredientes, detalle=detalle)
            receta.save()

            url_exitosa = reverse('recetas')
            return redirect(url_exitosa)

    else:
        formulario = form_recetas()
        contexto = {'formulario': formulario}
        http_response = render(
            request=request,
            template_name='recetas/recetas_agregar.html',
            context=contexto,
        )
        return http_response


def vista_recetas_buscar(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        categoria = recetas.objects.filter(categoria__icontains=busqueda)
        contexto = {
            "recetas": categoria,
        }
        http_response = render(
            request=request,
            template_name='recetas/recetas.html',
            context=contexto,
        )
        return http_response


def vista_recetas_detalle(request, pk):
    receta = get_object_or_404(recetas, id=pk)
    contexto = {
        "receta": receta,
    }
    return render(request, 'recetas/recetas_detalle.html', context=contexto)


@login_required
def vista_recetas_editar(request, pk):
    receta = recetas.objects.get(id=pk)
    if request.method == "POST":
        formulario = form_recetas(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            receta.autor = request.user
            receta.fecha = datetime.now().date()
            receta.titulo = data["titulo"]
            receta.categoria = data["categoria"]
            receta.ingredientes = data["ingredientes"]
            receta.detalle = data["detalle"]
            receta.save()

            url_exitosa = reverse('recetas_autor')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': receta.titulo,
            'categoria': receta.categoria,
            'ingredientes': receta.ingredientes,
            'detalle': receta.detalle,
        }
        formulario = form_recetas(initial=inicial)
    return render(
        request=request,
        template_name='recetas/recetas_agregar.html',
        context={'formulario': formulario},
    )


@login_required
def vista_recetas_eliminar(request, pk):
    receta = recetas.objects.get(id=pk)
    if request.method == "POST":
        receta.delete()
        url_exitosa = reverse('recetas_autor')
        return redirect(url_exitosa)
