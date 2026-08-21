from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.usuario import Usuario


def editar_perfil(request):

    if "usuario_id" not in request.session:

        messages.error(
            request,
            "Debe iniciar sesión."
        )

        return redirect("/auth/")

    usuario = Usuario.objects.filter(
        usu_id=request.session["usuario_id"]
    ).first()

    if usuario is None:

        request.session.flush()

        messages.error(
            request,
            "Su sesión ya no es válida."
        )

        return redirect("/auth/")

    if request.method == "POST":

        nombre = request.POST.get("nombre", "").strip()
        apellido = request.POST.get("apellido", "").strip()
        telefono = request.POST.get("telefono", "").strip()

        if not nombre:

            messages.error(
                request,
                "El nombre es obligatorio."
            )

            return redirect("/editar-perfil/")

        usuario.usu_nombre = nombre
        usuario.usu_apellido = apellido
        usuario.usu_telefono = telefono

        usuario.save()

        # Actualizamos también el nombre guardado en la sesión
        request.session["usuario_nombre"] = usuario.usu_nombre

        messages.success(
            request,
            "Tus datos se actualizaron correctamente."
        )

        return redirect("/perfil/")

    return render(
        request,
        "editar_perfil.html",
        {
            "usuario": usuario
        }
    )