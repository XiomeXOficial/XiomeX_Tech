from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

from ...models.producto import Producto
from ...models.categoria import Categoria
from ...permisos_vistas import requerir_administrador


def productos_panel(request):

    acceso = requerir_administrador(request)

    if acceso:
        return acceso

    # =====================================================
    # PROCESAR ACCIONES
    # =====================================================

    if request.method == "POST":

        accion = request.POST.get("accion")

        # =================================================
        # EDITAR PRODUCTO
        # =================================================

        if accion == "editar":

            producto_id = request.POST.get("producto_id")

            try:
                producto = Producto.objects.get(
                    prod_id=producto_id
                )
            except Producto.DoesNotExist:

                messages.error(
                    request,
                    "El producto no existe."
                )

                return redirect("productos_panel")

            nombre = request.POST.get(
                "nombre",
                ""
            ).strip()

            descripcion = request.POST.get(
                "descripcion",
                ""
            ).strip()

            precio = request.POST.get(
                "precio",
                ""
            ).strip()

            stock = request.POST.get(
                "stock",
                ""
            ).strip()

            estado = request.POST.get(
                "estado",
                ""
            ).strip()

            categoria_id = request.POST.get(
                "categoria_id"
            )

            # ---------------------------------------------
            # VALIDACIONES
            # ---------------------------------------------

            if not nombre:

                messages.error(
                    request,
                    "El nombre del producto es obligatorio."
                )

                return redirect("productos_panel")

            if not precio:

                messages.error(
                    request,
                    "El precio del producto es obligatorio."
                )

                return redirect("productos_panel")

            if not stock:

                messages.error(
                    request,
                    "El stock del producto es obligatorio."
                )

                return redirect("productos_panel")

            try:

                producto.prod_precio = precio
                producto.prod_stock = int(stock)

            except (ValueError, TypeError):

                messages.error(
                    request,
                    "El precio o el stock no tienen un valor válido."
                )

                return redirect("productos_panel")

            # ---------------------------------------------
            # DATOS DEL PRODUCTO
            # ---------------------------------------------

            producto.prod_nombre = nombre
            producto.prod_descripcion = descripcion
            producto.prod_estado = estado

            # ---------------------------------------------
            # CATEGORÍA
            # ---------------------------------------------

            if categoria_id:

                try:

                    categoria = Categoria.objects.get(
                        catg_id=categoria_id
                    )

                    producto.categoria = categoria

                except Categoria.DoesNotExist:

                    messages.error(
                        request,
                        "La categoría seleccionada no existe."
                    )

                    return redirect("productos_panel")

            else:

                producto.categoria = None

            # ---------------------------------------------
            # IMAGEN
            # ---------------------------------------------

            if request.FILES.get("imagen"):

                imagen_anterior = producto.prod_img

                producto.prod_img = request.FILES.get(
                    "imagen"
                )

                producto.save()

                if imagen_anterior:

                    try:

                        imagen_anterior.delete(
                            save=False
                        )

                    except Exception:
                        pass

            else:

                producto.save()

            messages.success(
                request,
                "Producto actualizado correctamente."
            )

            return redirect("productos_panel")

        # =================================================
        # ELIMINAR PRODUCTO
        # =================================================

        elif accion == "eliminar":

            producto_id = request.POST.get(
                "producto_id"
            )

            try:

                producto = Producto.objects.get(
                    prod_id=producto_id
                )

            except Producto.DoesNotExist:

                messages.error(
                    request,
                    "El producto no existe."
                )

                return redirect("productos_panel")

            nombre_producto = producto.prod_nombre
            imagen = producto.prod_img

            try:

                producto.delete()

                # Eliminamos también el archivo físico

                if imagen:

                    try:

                        imagen.delete(
                            save=False
                        )

                    except Exception:
                        pass

                messages.success(
                    request,
                    f'El producto "{nombre_producto}" fue eliminado correctamente.'
                )

            except Exception:

                messages.error(
                    request,
                    "No se pudo eliminar el producto."
                )

            return redirect(
                "productos_panel"
            )

    # =====================================================
    # OBTENER BÚSQUEDA
    # =====================================================

    busqueda = request.GET.get(
        "q",
        ""
    ).strip()

    # =====================================================
    # OBTENER PRODUCTOS
    # =====================================================

    productos = Producto.objects.select_related(
        "categoria"
    ).all()

    # =====================================================
    # FILTRAR PRODUCTOS
    # =====================================================

    if busqueda:

        productos = productos.filter(
            Q(prod_nombre__icontains=busqueda)
            |
            Q(prod_id__icontains=busqueda)
            |
            Q(categoria__catg_nombre__icontains=busqueda)
        )

    # =====================================================
    # ORDENAR PRODUCTOS
    # =====================================================

    productos = productos.order_by(
        "prod_nombre"
    )

    # =====================================================
    # PAGINACIÓN
    # =====================================================

    paginator = Paginator(
        productos,
        20
    )

    numero_pagina = request.GET.get(
        "page"
    )

    productos = paginator.get_page(
        numero_pagina
    )

    # =====================================================
    # CATEGORÍAS
    # =====================================================

    categorias = Categoria.objects.all().order_by(
        "catg_nombre"
    )

    # =====================================================
    # RENDER
    # =====================================================

    return render(
        request,
        "panel_administrador/productos_panel.html",
        {
            "productos": productos,
            "categorias": categorias,
            "busqueda": busqueda,
        }
    )
    
def buscar_productos(request):

    acceso = requerir_administrador(request)

    if acceso:
        return acceso

    busqueda = request.GET.get(
        "q",
        ""
    ).strip()

    if not busqueda:
        return JsonResponse(
            {
                "productos": []
            }
        )

    productos = Producto.objects.select_related(
        "categoria"
    ).filter(
        Q(prod_nombre__icontains=busqueda)
        |
        Q(prod_id__icontains=busqueda)
        |
        Q(categoria__catg_nombre__icontains=busqueda)
    ).order_by(
        "prod_nombre"
    )[:5]

    resultados = []

    for producto in productos:

        resultados.append(
            {
                "id": producto.prod_id,
                "nombre": producto.prod_nombre,
                "descripcion": producto.prod_descripcion or "",
                "precio": str(producto.prod_precio),
                "stock": producto.prod_stock,
                "estado": producto.prod_estado,
                "categoria_id": (
                    producto.categoria.catg_id
                    if producto.categoria
                    else ""
                ),
                "categoria_nombre": (
                    producto.categoria.catg_nombre
                    if producto.categoria
                    else "Sin categoría"
                ),
            }
        )

    return JsonResponse(
        {
            "productos": resultados
        }
    )