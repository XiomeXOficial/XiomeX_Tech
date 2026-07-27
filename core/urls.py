from django.urls import path

from .views.index import index
from .views.auth import auth
from .views.productos import productos
from .views.servicios import servicios
from .views.perfil import perfil
from .views.carrito import carrito

urlpatterns = [
    path("", index, name="index"),
    path("auth/", auth, name="auth"),
    path("productos/", productos, name="productos"),
    path("servicios/", servicios, name="servicios"),
    path("perfil/", perfil, name="perfil"),
    path("carrito/", carrito, name="carrito"),
]