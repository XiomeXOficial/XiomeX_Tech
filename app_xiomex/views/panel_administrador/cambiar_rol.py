from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.usuario import Usuario
from ...permisos_vistas import requerir_superadministrador


def cambiar_rol(request, usuario_id):

    acceso = requerir_superadministrador(request)

    if acceso:
        return acceso

    usuario = Usuario.objects.filter(
        usu_id=usuario_id
    ).first()

    if usuario is None:
        messages.error(
            request,
            "El usuario no existe."
        )

        return redirect("/panel-administrador/usuarios/")

    # El superadministrador original está protegido
    if usuario.usu_superadmin_original:

        messages.error(
            request,
            "El superadministrador original está protegido."
        )

        return redirect("/panel-administrador/usuarios/")

    if request.method == "POST":

        nuevo_rol = request.POST.get(
            "rol"
        )

        roles_validos = [
            "cliente",
            "administrador",
            "superadministrador"
        ]

        if nuevo_rol not in roles_validos:

            messages.error(
                request,
                "El rol seleccionado no es válido."
            )

            return redirect(
                f"/panel-administrador/usuarios/{usuario_id}/rol/"
            )

        usuario.usu_rol = nuevo_rol

        # Si deja de ser superadministrador,
        # nunca puede conservar la marca de original.
        usuario.usu_superadmin_original = False

        usuario.save()

        messages.success(
            request,
            "El rol del usuario fue actualizado correctamente."
        )

        return redirect(
            "/panel-administrador/usuarios/"
        )

    return render(
        request,
        "panel_administrador/cambiar_rol.html",
        {
            "usuario": usuario
        }
    )