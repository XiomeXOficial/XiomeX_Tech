from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone

from datetime import timedelta
import secrets

from ...models.usuario import Usuario


def ingresar_correo(request):

    # =====================================================
    # PROCESAR CORREO
    # =====================================================

    if request.method == "POST":

        correo = request.POST.get(
            "correo",
            ""
        ).strip()


        # =================================================
        # BUSCAR USUARIO
        # =================================================

        usuario = Usuario.objects.filter(
            usu_correo__iexact=correo
        ).first()


        if usuario is None:

            messages.error(
                request,
                "No existe una cuenta asociada a ese correo."
            )

            return redirect(
                "recuperar_contrasena"
            )


        # =================================================
        # LIMPIAR RECUPERACIÓN ANTERIOR
        # =================================================

        request.session.pop(
            "recuperacion_usuario_id",
            None
        )

        request.session.pop(
            "recuperacion_correo",
            None
        )

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


        # =================================================
        # GENERAR CÓDIGO
        # =================================================

        codigo = str(
            secrets.randbelow(900000) + 100000
        )


        # =================================================
        # GUARDAR DATOS EN SESIÓN
        # =================================================

        request.session[
            "recuperacion_usuario_id"
        ] = usuario.usu_id

        request.session[
            "recuperacion_correo"
        ] = usuario.usu_correo

        request.session[
            "recuperacion_codigo"
        ] = codigo

        request.session[
            "recuperacion_expira"
        ] = (
            timezone.now()
            + timedelta(minutes=10)
        ).isoformat()

        request.session[
            "recuperacion_verificada"
        ] = False


        # =================================================
        # ENVIAR CORREO
        # =================================================

        send_mail(

            "Recuperación de contraseña - XiomeX Tech",

            f"""
Hola.

Hemos recibido una solicitud para recuperar
la contraseña de tu cuenta de XiomeX Tech.

Tu código de verificación es:

{codigo}

Este código expirará en 10 minutos.

Si no solicitaste este cambio, puedes ignorar
este correo.
            """,

            None,

            [usuario.usu_correo],

            fail_silently=False,
        )


        # =================================================
        # MENSAJE
        # =================================================

        messages.success(
            request,
            "Te hemos enviado un código de verificación a tu correo."
        )


        # =================================================
        # IR A VERIFICACIÓN
        # =================================================

        return redirect(
            "verificar_recuperacion"
        )


    # =====================================================
    # MOSTRAR PÁGINA
    # =====================================================

    return render(
        request,
        "ingresar_correo.html"
    )