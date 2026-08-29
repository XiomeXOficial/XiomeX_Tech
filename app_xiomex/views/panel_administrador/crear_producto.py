from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.producto import Producto
from ...models.categoria import Categoria
from ...permisos_vistas import requerir_administrador


def crear_producto(request):

    acceso = requerir_administrador(request)

    if acceso:
        return acceso

    categorias = Categoria.objects.all().order_by("catg_nombre")

    if request.method == "POST":

        nombre = request.POST.get("nombre", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        precio = request.POST.get("precio", "").strip()
        stock = request.POST.get("stock", "").strip()
        categoria_id = request.POST.get("categoria")
        estado = request.POST.get("estado", "activo")
        imagen = request.FILES.get("imagen")

        if not nombre:
            messages.error(
                request,
                "El nombre del producto es obligatorio."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        if not precio:
            messages.error(
                request,
                "El precio del producto es obligatorio."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        if not stock:
            messages.error(
                request,
                "El stock del producto es obligatorio."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        try:

            precio = float(precio)
            stock = int(stock)

        except ValueError:

            messages.error(
                request,
                "El precio o el stock no tienen un formato válido."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        if precio < 0:
            messages.error(
                request,
                "El precio no puede ser negativo."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        if stock < 0:
            messages.error(
                request,
                "El stock no puede ser negativo."
            )

            return render(
                request,
                "panel_administrador/crear_producto.html",
                {
                    "categorias": categorias
                }
            )

        categoria = None

        if categoria_id:

            try:

                categoria = Categoria.objects.get(
                    catg_id=categoria_id
                )

            except Categoria.DoesNotExist:

                messages.error(
                    request,
                    "La categoría seleccionada no existe."
                )

                return render(
                    request,
                    "panel_administrador/crear_producto.html",
                    {
                        "categorias": categorias
                    }
                )

        Producto.objects.create(
            prod_nombre=nombre,
            prod_descripcion=descripcion,
            prod_precio=precio,
            prod_stock=stock,
            prod_img=imagen,
            prod_estado=estado,
            categoria=categoria
        )

        messages.success(
            request,
            "Producto creado correctamente."
        )

        return redirect("productos_panel")

    return render(
        request,
        "panel_administrador/crear_producto.html",
        {
            "categorias": categorias
        }
    )