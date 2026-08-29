document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // FILTRO DE CATEGORÍAS
    // =====================================================

    const botonFiltros =
        document.getElementById("boton-filtros");

    const filtrosCategorias =
        document.getElementById("filtros-categorias");


    if (botonFiltros && filtrosCategorias) {

        botonFiltros.addEventListener("click", function () {

            const abierto =
                filtrosCategorias.classList.toggle("mostrar");

            const icono =
                botonFiltros.querySelector("i");


            if (icono) {

                if (abierto) {

                    icono.classList.remove("fa-plus");
                    icono.classList.add("fa-minus");

                } else {

                    icono.classList.remove("fa-minus");
                    icono.classList.add("fa-plus");

                }

            }

        });

    }


    // =====================================================
    // AÑADIR AL CARRITO
    // =====================================================

    const botonesCarrito =
        document.querySelectorAll(
            ".producto-agregar-carrito"
        );


    botonesCarrito.forEach(function (boton) {

        boton.addEventListener("click", function () {

            /*
                FUNCIONALIDAD CARRITO PENDIENTE.
            */

        });

    });

});