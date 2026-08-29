from django.shortcuts import render, redirect
from django.contrib import messages

def logout(request):

    request.session.flush()

    messages.success(
        request,
        "Sesión cerrada correctamente."
    )

    return redirect("/auth/")