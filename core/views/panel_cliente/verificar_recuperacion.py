from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from datetime import datetime


def verificar_recuperacion(request):

    # =====================================================
    # COMPROBAR RECUPERACIÓN PENDIENTE
    # =====================================================

    if "recuperacion_codigo" not in request.session:

        messages.error(
            request,
            "No hay ninguna recuperación de contraseña pendiente."
        )

        return redirect(
            "recuperar_contrasena"
        )


    # =====================================================
    # PROCESAR CÓDIGO
    # =====================================================

    if request.method == "POST":

        codigo_ingresado = request.POST.get(
            "codigo",
            ""
        ).strip()

        codigo_correcto = request.session.get(
            "recuperacion_codigo"
        )

        codigo_expira = request.session.get(
            "recuperacion_expira"
        )


        # =================================================
        # COMPROBAR EXPIRACIÓN
        # =================================================

        if codigo_expira:

            fecha_expiracion = datetime.fromisoformat(
                codigo_expira
            )

            if timezone.now() > fecha_expiracion:

                request.session.pop(
                    "recuperacion_codigo",
                    None
                )

                request.session.pop(
                    "recuperacion_expira",
                    None
                )

                request.session.pop(
                    "recuperacion_verificada",
                    None
                )

                messages.error(
                    request,
                    "El código de verificación ha expirado."
                )

                return redirect(
                    "verificar_recuperacion"
                )


        # =================================================
        # COMPROBAR CÓDIGO
        # =================================================

        if codigo_ingresado != codigo_correcto:

            messages.error(
                request,
                "El código de verificación es incorrecto."
            )

            return redirect(
                "verificar_recuperacion"
            )


        # =================================================
        # CÓDIGO CORRECTO
        # =================================================

        request.session[
            "recuperacion_verificada"
        ] = True


        # =================================================
        # EL CÓDIGO YA NO SE NECESITA
        # =================================================

        request.session.pop(
            "recuperacion_codigo",
            None
        )

        request.session.pop(
            "recuperacion_expira",
            None
        )


        # =================================================
        # MENSAJE
        # =================================================

        messages.success(
            request,
            "Correo verificado correctamente."
        )


        # =================================================
        # IR A CAMBIAR CONTRASEÑA
        # =================================================

        return redirect(
            "cambiar_contrasena"
        )


    # =====================================================
    # MOSTRAR PÁGINA
    # =====================================================

    return render(
        request,
        "verificar_recuperacion.html"
    )