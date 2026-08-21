from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from ...models.usuario import Usuario


def cambiar_contrasena(request):

    # =====================================================
    # DETERMINAR DE DÓNDE VIENE EL USUARIO
    # =====================================================

    recuperacion_verificada = request.session.get(
        "recuperacion_verificada",
        False
    )

    usuario_id = None

    modo_recuperacion = False


    # =====================================================
    # CASO 1
    # RECUPERACIÓN DE CONTRASEÑA
    # =====================================================

    if recuperacion_verificada:

        usuario_id = request.session.get(
            "recuperacion_usuario_id"
        )

        if usuario_id is None:

            messages.error(
                request,
                "La recuperación de contraseña no es válida."
            )

            return redirect(
                "auth"
            )

        modo_recuperacion = True


    # =====================================================
    # CASO 2
    # USUARIO LOGUEADO
    # =====================================================

    elif "usuario_id" in request.session:

        usuario_id = request.session.get(
            "usuario_id"
        )

        modo_recuperacion = False


    # =====================================================
    # NO HAY USUARIO
    # =====================================================

    else:

        messages.error(
            request,
            "Debe iniciar sesión."
        )

        return redirect(
            "auth"
        )


    # =====================================================
    # BUSCAR USUARIO
    # =====================================================

    usuario = Usuario.objects.filter(
        usu_id=usuario_id
    ).first()

    if usuario is None:

        messages.error(
            request,
            "No se encontró la cuenta."
        )

        return redirect(
            "auth"
        )


    # =====================================================
    # PROCESAR FORMULARIO
    # =====================================================

    if request.method == "POST":

        password_nueva = request.POST.get(
            "password_nueva",
            ""
        ).strip()

        confirmar_password = request.POST.get(
            "confirmar_password",
            ""
        ).strip()


        # -------------------------------------------------
        # COMPROBAR QUE NO ESTÉN VACÍAS
        # -------------------------------------------------

        if not password_nueva or not confirmar_password:

            messages.error(
                request,
                "Debes completar ambos campos."
            )

            return redirect(
                "cambiar_contrasena"
            )


        # -------------------------------------------------
        # COMPROBAR CONTRASEÑAS
        # -------------------------------------------------

        if password_nueva != confirmar_password:

            messages.error(
                request,
                "Las contraseñas no coinciden."
            )

            return redirect(
                "cambiar_contrasena"
            )


        # -------------------------------------------------
        # GUARDAR NUEVA CONTRASEÑA
        # -------------------------------------------------

        usuario.usu_contraseña = make_password(
            password_nueva
        )

        usuario.save(
            update_fields=[
                "usu_contraseña"
            ]
        )


        # =================================================
        # RECUPERACIÓN
        # =================================================

        if modo_recuperacion:

            request.session.pop(
                "recuperacion_usuario_id",
                None
            )

            request.session.pop(
                "recuperacion_correo",
                None
            )

            request.session.pop(
                "recuperacion_verificada",
                None
            )

            messages.success(
                request,
                "Tu contraseña ha sido cambiada correctamente."
            )

            return redirect(
                "auth"
            )


        # =================================================
        # USUARIO LOGUEADO
        # =================================================

        messages.success(
            request,
            "Tu contraseña ha sido cambiada correctamente."
        )

        return redirect(
            "seguridad"
        )


    # =====================================================
    # MOSTRAR HTML
    # =====================================================

    return render(
        request,
        "cambiar_contrasena.html",
        {
            "modo_recuperacion": modo_recuperacion
        }
    )