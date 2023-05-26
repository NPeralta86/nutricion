from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def vista_index(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='agenda/index.html',
        context=contexto,
    )
    return http_response


def vista_about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='agenda/about.html',
        context=contexto,
    )
    return http_response
