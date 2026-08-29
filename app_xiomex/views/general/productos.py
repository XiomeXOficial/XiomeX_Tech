from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from ...models.producto import Producto
from ...models.categoria import Categoria


def productos(request):

    # =====================================================
    # BÚSQUEDA
    # =====================================================

    busqueda = request.GET.get("q", "").strip()

    # =====================================================
    # OBTENER PRODUCTOS
    # =====================================================

    productos = Producto.objects.select_related(
        "categoria"
    ).filter(
        prod_estado="activo"
    )

    # =====================================================
    # FILTRAR POR BÚSQUEDA
    # =====================================================

    if busqueda:
        productos = productos.filter(
            Q(prod_nombre__icontains=busqueda)
            |
            Q(prod_descripcion__icontains=busqueda)
        )

    # =====================================================
    # ORDENAR
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
        "general/productos.html",
        {
            "productos": productos,
            "categorias": categorias,
            "busqueda": busqueda,
        }
    )