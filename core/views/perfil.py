from django.shortcuts import render


def perfil(request):
    return render(request, "profile/perfil.html")