from django.shortcuts import render


def carrito(request):
    return render(request, "panel_cliente/carrito.html")