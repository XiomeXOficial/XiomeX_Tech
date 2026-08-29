from django.shortcuts import render, redirect, get_object_or_404

from ...models.categoria import Categoria
from ...permisos_vistas import requerir_administrador


def categorias_panel(request):

    acceso = requerir_administrador(request)

    if acceso:
        return acceso


    # =====================================================
    # OPERACIONES POST
    # =====================================================

    if request.method == "POST":

        accion = request.POST.get("accion")


        # =================================================
        # CREAR CATEGORÍA
        # =================================================

        if accion == "crear":

            nombre = request.POST.get(
                "nombre",
                ""
            ).strip()


            if nombre:

                Categoria.objects.create(
                    catg_nombre=nombre
                )


            return redirect("categorias")


        # =================================================
        # EDITAR CATEGORÍA
        # =================================================

        elif accion == "editar":

            categoria_id = request.POST.get(
                "categoria_id"
            )

            nombre = request.POST.get(
                "nombre",
                ""
            ).strip()


            categoria = get_object_or_404(
                Categoria,
                catg_id=categoria_id
            )


            if nombre:

                categoria.catg_nombre = nombre

                categoria.save()


            return redirect("categorias")


        # =================================================
        # ELIMINAR CATEGORÍA
        # =================================================

        elif accion == "eliminar":

            categoria_id = request.POST.get(
                "categoria_id"
            )


            categoria = get_object_or_404(
                Categoria,
                catg_id=categoria_id
            )


            categoria.delete()


            return redirect("categorias")


    # =====================================================
    # MOSTRAR CATEGORÍAS
    # =====================================================

    categorias = Categoria.objects.all().order_by(
        "catg_nombre"
    )


    return render(
        request,
        "panel_administrador/categorias.html",
        {
            "categorias": categorias
        }
    )