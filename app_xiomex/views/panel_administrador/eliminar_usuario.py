from django.shortcuts import redirect

from django.contrib import messages

from ...models.usuario import Usuario

from .permisos_administracion import puede_administrar


def eliminar_usuario(request, usuario_id):

    # =====================================================
    # COMPROBAR SESIÓN
    # =====================================================

    if "usuario_id" not in request.session:
        return redirect("auth")


    # =====================================================
    # OBTENER USUARIO ACTUAL
    # =====================================================

    usuario_actual = Usuario.objects.filter(
        usu_id=request.session["usuario_id"]
    ).first()

    if usuario_actual is None:
        return redirect("auth")


    # =====================================================
    # OBTENER USUARIO A ELIMINAR
    # =====================================================

    usuario = Usuario.objects.filter(
        usu_id=usuario_id
    ).first()

    if usuario is None:

        messages.error(
            request,
            "El usuario no existe."
        )

        return redirect("usuarios")


    # =====================================================
    # COMPROBAR PERMISOS
    # =====================================================

    if not puede_administrar(
        usuario_actual,
        usuario
    ):

        messages.error(
            request,
            "No tienes permisos para eliminar este usuario."
        )

        return redirect("usuarios")


    # =====================================================
    # ELIMINAR
    # =====================================================
    if usuario.usu_img and usuario.usu_img.name != "default_perfil.png":
        usuario.usu_img.delete(save=False)
    
    usuario.delete()


    # =====================================================
    # ÉXITO
    # =====================================================

    messages.success(
        request,
        "Usuario eliminado correctamente."
    )

    return redirect("usuarios")