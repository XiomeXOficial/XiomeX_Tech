from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("auth/", views.auth, name="auth"),
    path("productos/", views.productos, name="productos"),
    path("servicios/", views.servicios, name="servicios"),
    path("perfil/", views.perfil, name="perfil"),
    path("carrito/", views.carrito, name="carrito"),
]