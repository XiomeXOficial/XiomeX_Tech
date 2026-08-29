from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.utils import timezone

from ...models.usuario import Usuario


def verificar_correo(request):

    # =====================================================
    # COMPROBAR SI EXISTE UNA VERIFICACIÓN PENDIENTE
    # =====================================================

    if "codigo_verificacion" not in request.session:

        messages.error(
            request,
            "No hay ninguna verificación pendiente."
        )

        return redirect("/auth/?mode=register")


    # =====================================================
    # PROCESAR CÓDIGO
    # =====================================================

    if request.method == "POST":


        # =================================================
        # OBTENER CÓDIGO
        # =================================================

        codigo_ingresado = request.POST.get(
            "codigo",
            ""
        ).strip()


        codigo_correcto = request.session.get(
            "codigo_verificacion"
        )


        codigo_expira = request.session.get(
            "codigo_expira"
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
                    "codigo_verificacion",
                    None
                )

                request.session.pop(
                    "codigo_expira",
                    None
                )


                messages.error(
                    request,
                    "El código de verificación ha expirado."
                )


                return redirect(
                    "/verificar-correo/"
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
                "/verificar-correo/"
            )


        # =================================================
        # CREAR USUARIO
        # =================================================

        Usuario.objects.create(

            usu_nombre=request.session[
                "registro_nombre"
            ],

            usu_apellido=request.session[
                "registro_apellido"
            ],

            usu_correo=request.session[
                "registro_correo"
            ],

            usu_telefono=request.session[
                "registro_telefono"
            ],

            usu_contraseña=make_password(
                request.session[
                    "registro_password"
                ]
            )

        )


        # =================================================
        # LIMPIAR SESIÓN
        # =================================================

        request.session.pop(
            "registro_nombre",
            None
        )

        request.session.pop(
            "registro_apellido",
            None
        )

        request.session.pop(
            "registro_correo",
            None
        )

        request.session.pop(
            "registro_telefono",
            None
        )

        request.session.pop(
            "registro_password",
            None
        )

        request.session.pop(
            "codigo_verificacion",
            None
        )

        request.session.pop(
            "codigo_expira",
            None
        )


        # =================================================
        # ÉXITO
        # =================================================

        messages.success(
            request,
            "Cuenta creada correctamente."
        )


        return redirect("/auth/")


    # =====================================================
    # MOSTRAR PÁGINA
    # =====================================================

    return render(
        request,
        "panel_cliente/verificar_correo.html"
    )