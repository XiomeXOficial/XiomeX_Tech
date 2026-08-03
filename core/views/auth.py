from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from ..models.usuario import Usuario

def auth(request):

    mode = request.GET.get("mode", "login")

    if request.method == "POST":
        
        if request.POST.get("formulario") == "login":

            correo = request.POST.get("correo")
            password = request.POST.get("password")
            
            usuario = Usuario.objects.filter(usu_correo=correo).first()
            
            if usuario is None:
            
                messages.error(request, "Correo o contraseña incorrectos.")
                return redirect("/auth/")
        
            if not check_password(
                password,
                usuario.usu_contraseña
            ):

                messages.error(request,"Correo o contraseña incorrectos.")
                return redirect("/auth/")
            
            request.session["usuario_id"] = usuario.usu_id
            request.session["usuario_nombre"] = usuario.usu_nombre
            request.session["usuario_rol"] = usuario.usu_rol

            messages.success(request, "Bienvenido nuevamente.")

            return redirect("/perfil/")

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

            Usuario.objects.create(

                usu_nombre=nombre,
                usu_apellido=apellido,
                usu_correo=correo,
                usu_telefono=telefono,
                usu_contraseña=make_password(password)

            )

            messages.success(request, "Cuenta creada correctamente.")
            return redirect("/auth/")

    return render(request, "auth.html", {"mode": mode})
