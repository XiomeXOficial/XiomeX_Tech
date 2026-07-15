from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def auth(request):
    mode = request.GET.get("mode", "login")
    return render(request,"auth.html",{"mode": mode})

def productos(request):
    return render(request, "productos.html")

def servicios(request):
    return render(request, "servicios.html")

def perfil(request):
    return render(request, "perfil.html")

def carrito(request):
    return render(request, "carrito.html")
# Create your views here.
