from django.shortcuts import render, redirect
from django.shortcuts import render

from ...models.usuario import Usuario
from ...permisos_vistas import requerir_superadministrador

from .permisos_administracion import puede_administrar


def usuarios(request):

    acceso = requerir_superadministrador(request)

    if acceso:
        return acceso

    usuario_actual = Usuario.objects.filter(
        usu_id=request.session["usuario_id"]
    ).first()

    if usuario_actual is None:
        return redirect("auth")

    usuarios = Usuario.objects.all().order_by("usu_nombre")

    for usuario in usuarios:
        usuario.puede_administrar = puede_administrar(
            usuario_actual,
            usuario
        )

    return render(
        request,
        "panel_administrador/usuarios.html",
        {
            "usuarios": usuarios
        }
    )