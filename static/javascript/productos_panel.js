document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // FUNCIONES GENERALES
    // =====================================================

    function abrirModal(id) {

        const modal = document.getElementById(id);

        if (modal) {
            modal.classList.add("mostrar");
        }

    }


    function cerrarModal(id) {

        const modal = document.getElementById(id);

        if (modal) {
            modal.classList.remove("mostrar");
        }

    }


    // =====================================================
    // CERRAR MODALES
    // =====================================================

    const botonesCerrar =
        document.querySelectorAll("[data-cerrar]");

    botonesCerrar.forEach(function (boton) {

        boton.addEventListener("click", function () {

            const id =
                boton.getAttribute("data-cerrar");

            cerrarModal(id);

        });

    });


    // =====================================================
    // EDITAR PRODUCTO
    // =====================================================

    const botonesEditar =
        document.querySelectorAll(".producto-editar");

    botonesEditar.forEach(function (boton) {

        boton.addEventListener("click", function () {

            // -------------------------------------------------
            // OBTENER DATOS DEL PRODUCTO
            // -------------------------------------------------

            const id =
                boton.getAttribute("data-id") || "";

            const nombre =
                boton.getAttribute("data-nombre") || "";

            const descripcion =
                boton.getAttribute("data-descripcion") || "";

            const precio =
                boton.getAttribute("data-precio") || "";

            const stock =
                boton.getAttribute("data-stock") || "";

            const estado =
                boton.getAttribute("data-estado") || "activo";

            const categoria =
                boton.getAttribute("data-categoria") || "";


            // -------------------------------------------------
            // MOSTRAR DATOS EN EL FORMULARIO
            // -------------------------------------------------

            const campoId =
                document.getElementById(
                    "editar-producto-id"
                );

            if (campoId) {
                campoId.value = id;
            }


            const campoNombre =
                document.getElementById(
                    "editar-nombre"
                );

            if (campoNombre) {
                campoNombre.value = nombre;
            }


            const campoDescripcion =
                document.getElementById(
                    "editar-descripcion"
                );

            if (campoDescripcion) {
                campoDescripcion.value = descripcion;
            }


            // -------------------------------------------------
            // PRECIO
            // -------------------------------------------------

            const campoPrecio =
                document.getElementById(
                    "editar-precio"
                );

            if (campoPrecio) {

                let precioLimpio =
                    precio
                        .toString()
                        .trim()
                        .replace(",", ".");

                campoPrecio.value =
                    precioLimpio;

            }


            // -------------------------------------------------
            // STOCK
            // -------------------------------------------------

            const campoStock =
                document.getElementById(
                    "editar-stock"
                );

            if (campoStock) {
                campoStock.value = stock;
            }


            // -------------------------------------------------
            // ESTADO
            // -------------------------------------------------

            const campoEstado =
                document.getElementById(
                    "editar-estado"
                );

            if (campoEstado) {
                campoEstado.value = estado;
            }


            // -------------------------------------------------
            // CATEGORÍA
            // -------------------------------------------------

            const campoCategoria =
                document.getElementById(
                    "editar-categoria"
                );

            if (campoCategoria) {
                campoCategoria.value = categoria;
            }


            // -------------------------------------------------
            // LIMPIAR IMAGEN
            // -------------------------------------------------

            const campoImagen =
                document.getElementById(
                    "editar-imagen"
                );

            if (campoImagen) {
                campoImagen.value = "";
            }


            // -------------------------------------------------
            // ABRIR MODAL
            // -------------------------------------------------

            abrirModal(
                "modal-editar-producto"
            );

        });

    });


    // =====================================================
    // ELIMINAR PRODUCTO
    // =====================================================

    const botonesEliminar =
        document.querySelectorAll(
            ".producto-eliminar"
        );

    botonesEliminar.forEach(function (boton) {

        boton.addEventListener(
            "click",
            function () {

                const id =
                    boton.getAttribute("data-id") || "";

                const nombre =
                    boton.getAttribute("data-nombre") || "";


                const campoId =
                    document.getElementById(
                        "eliminar-producto-id"
                    );

                if (campoId) {
                    campoId.value = id;
                }


                const campoNombre =
                    document.getElementById(
                        "eliminar-producto-nombre"
                    );

                if (campoNombre) {
                    campoNombre.textContent = nombre;
                }


                abrirModal(
                    "modal-eliminar-producto"
                );

            }
        );

    });


    // =====================================================
    // CERRAR AL HACER CLICK FUERA DEL MODAL
    // =====================================================

    const overlays =
        document.querySelectorAll(
            ".producto-modal-overlay"
        );

    overlays.forEach(function (overlay) {

        overlay.addEventListener(
            "click",
            function (evento) {

                if (evento.target === overlay) {

                    overlay.classList.remove(
                        "mostrar"
                    );

                }

            }
        );

    });


    // =====================================================
    // CERRAR CON ESC
    // =====================================================

    document.addEventListener(
        "keydown",
        function (evento) {

            if (evento.key === "Escape") {

                overlays.forEach(
                    function (overlay) {

                        overlay.classList.remove(
                            "mostrar"
                        );

                    }
                );

            }

        }
    );

});