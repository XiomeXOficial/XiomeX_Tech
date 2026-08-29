from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.usuario import Usuario


def perfil(request):

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
            "su sesión ya no es válida."
        )
        
        return redirect ("/auth/")
    
    return render(
        request,
        "panel_cliente/perfil.html",
        {
            "usuario": usuario
        }
    )