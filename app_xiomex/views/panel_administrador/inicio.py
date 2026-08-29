from django.shortcuts import render

from ...permisos_vistas import requerir_administrador


def inicio(request):

    acceso = requerir_administrador(request)

    if acceso:
        return acceso

    return render(
        request,
        "panel_administrador/inicio.html"
    )