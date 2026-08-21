from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.usuario import Usuario

def seguridad(request):

    if "usuario_id" not in request.session:
        messages.error(
            request,
            "Debe iniciar sesión."
        )
        return redirect("auth")

    usuario = Usuario.objects.filter(
        usu_id=request.session["usuario_id"]
    ).first()

    if usuario is None:
        request.session.flush()
        messages.error(
            request,
            "No se encontró la cuenta."
        )
        return redirect("auth")

    return render(
        request,
        "seguridad.html",
        {
            "usuario": usuario
        }
    )

