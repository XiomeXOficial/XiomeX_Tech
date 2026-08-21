from django.urls import path

from .views.general.index import index
from .views.general.auth import auth
from .views.general.productos import productos
from .views.general.servicios import servicios
from .views.panel_cliente.perfil import perfil
from .views.general.carrito import carrito
from .views.general.logout import logout
from .views.panel_cliente.seguridad import seguridad

from .views.panel_cliente.verificar_correo import verificar_correo
from .views.panel_cliente.editar_perfil import editar_perfil
from .views.panel_cliente.cambiar_foto import cambiar_foto
from .views.panel_cliente.cambiar_contrasena import cambiar_contrasena
from .views.panel_cliente.ingresar_correo import ingresar_correo
from .views.panel_cliente.verificar_recuperacion import verificar_recuperacion

urlpatterns = [
    path("", index, name="index"),
    path("auth/", auth, name="auth"),
    path("productos/", productos, name="productos"),
    path("servicios/", servicios, name="servicios"),
    path("perfil/", perfil, name="perfil"),
    path("carrito/", carrito, name="carrito"),
    path("logout/", logout, name="logout"),
    path("seguridad/", seguridad, name="seguridad"),

    path("verificar-correo/", verificar_correo, name="verificar_correo"),
    path("editar-perfil/", editar_perfil, name="editar_perfil"),
    path("cambiar-foto/", cambiar_foto, name="cambiar_foto"),
    path("cambiar-contrasena/", cambiar_contrasena, name="cambiar_contrasena"),
    path("recuperar-contrasena/", ingresar_correo, name="recuperar_contrasena"),
    path("verificar-recuperacion/", verificar_recuperacion, name="verificar_recuperacion"),
]