from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone

import secrets

from ...models.usuario import Usuario

def auth(request):

    mode = request.GET.get("mode", "login")

    if request.method == "POST":
        
        if request.POST.get("formulario") == "login":

            correo = request.POST.get("correo")
            password = request.POST.get("password")
            
            usuario = Usuario.objects.filter(usu_correo=correo).first()
            
            if usuario is None:
            
                messages.error(request, "Correo o contraseña incorrectos.")
                return redirect("auth")
        
            if not check_password(
                password,
                usuario.usu_contraseña
            ):

                messages.error(request,"Correo o contraseña incorrectos.")
                return redirect("auth")
            
            request.session["usuario_id"] = usuario.usu_id
            request.session["usuario_nombre"] = usuario.usu_nombre
            request.session["usuario_rol"] = usuario.usu_rol

            messages.success(request, "Bienvenido nuevamente.")

            return redirect("perfil")

        if request.POST.get("formulario") == "registro":

            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            correo = request.POST.get("correo")
            telefono = request.POST.get("telefono")
            password = request.POST.get("password")
            confirmar_password = request.POST.get("confirmar_password")

            if password != confirmar_password:

                messages.error(
                    request,
                    "Las contraseñas no coinciden."
                )

                return redirect("/auth/?mode=register")

            if Usuario.objects.filter(usu_correo=correo).exists():

                messages.error(request, "Este correo ya está registrado.")
                return redirect("/auth/?mode=register")
            
            codigo = str(secrets.randbelow(900000)+100000)

            request.session["registro_nombre"] = nombre
            request.session["registro_apellido"] = apellido
            request.session["registro_correo"] = correo
            request.session["registro_telefono"] = telefono
            request.session["registro_password"] = password
            request.session["codigo_verificacion"] = codigo
            
            request.session["codigo_expira"] = (
                timezone.now() + timedelta(minutes=10)
            ).isoformat()
            
            send_mail(
                "Verificación de correo - XiomeX Tech",
                f"""
            Hola.

            Hemos recibido una solicitud para crear una cuenta
            en XiomeX Tech.

            Tu código de verificación es:

            {codigo}

            Ingresa este código en la página de verificación
            para confirmar tu correo electrónico y completar
            la creación de tu cuenta.

            Si no solicitaste crear una cuenta, puedes ignorar
            este correo.
                """,
                None,
                [correo],
                fail_silently=False,
            )

            messages.success(
                request,
                "Te hemos enviado un código de verificación a tu correo."
            )

            return redirect("verificar-correo")

    return render(request, "auth.html", {"mode": mode})
