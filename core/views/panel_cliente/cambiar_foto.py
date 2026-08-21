from django.shortcuts import redirect
from django.contrib import messages
from ...models.usuario import Usuario


def cambiar_foto(request):

    if "usuario_id" not in request.session:
        messages.error(request, "Debe iniciar sesión.")
        return redirect("/auth/")

    if request.method == "POST":
        usuario = Usuario.objects.filter(usu_id=request.session["usuario_id"]).first()

        if usuario is None:
            request.session.flush()
            messages.error(request, "Su sesión ya no es válida.")
            return redirect("/auth/")

        foto = request.FILES.get("foto")

        if foto:
            foto_anterior = usuario.usu_img
            usuario.usu_img = foto
            usuario.save()

            if foto_anterior and foto_anterior.name != "default.png":
                foto_anterior.delete(save=False)

            messages.success(request, "Foto de perfil actualizada correctamente.")

    return redirect("/perfil/")