document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // ELEMENTOS
    // =====================================================

    const buscador = document.getElementById(
        "buscar-producto"
    );

    const resultados = document.getElementById(
        "resultados-busqueda-productos"
    );

    if (!buscador || !resultados) {
        return;
    }


    // =====================================================
    // VARIABLES
    // =====================================================

    let temporizador = null;


    // =====================================================
    // ESCAPAR HTML
    // =====================================================

    function escaparHTML(texto) {

        const div = document.createElement("div");

        div.textContent = texto ?? "";

        return div.innerHTML;
    }


    // =====================================================
    // OCULTAR RESULTADOS
    // =====================================================

    function ocultarResultados() {

        resultados.innerHTML = "";

        resultados.classList.remove(
            "mostrar"
        );
    }


    // =====================================================
    // MOSTRAR RESULTADOS
    // =====================================================

    function mostrarResultados(productos) {

        resultados.innerHTML = "";

        if (!productos.length) {

            resultados.innerHTML = `
                <div class="busqueda-sin-resultados">
                    <i class="fa-solid fa-box-open"></i>
                    <span>No se encontraron productos.</span>
                </div>
            `;

            resultados.classList.add(
                "mostrar"
            );

            return;
        }


        productos.forEach(function (producto) {

            const elemento = document.createElement(
                "button"
            );

            elemento.type = "button";

            elemento.className =
                "resultado-busqueda-producto";


            elemento.innerHTML = `
                <div class="resultado-producto-icono">
                    <i class="fa-solid fa-box"></i>
                </div>

                <div class="resultado-producto-info">

                    <strong>
                        ${escaparHTML(producto.nombre)}
                    </strong>

                    <span>
                        ID #${producto.id}
                        ·
                        ${escaparHTML(producto.categoria_nombre)}
                    </span>

                </div>

                <i class="fa-solid fa-chevron-right resultado-producto-flecha"></i>
            `;


            // =================================================
            // CLICK EN PRODUCTO
            // =================================================

            elemento.addEventListener(
                "click",
                function () {

                    abrirProducto(producto);

                }
            );


            resultados.appendChild(
                elemento
            );

        });


        resultados.classList.add(
            "mostrar"
        );
    }


    // =====================================================
    // BUSCAR PRODUCTOS
    // =====================================================

    async function buscarProductos(texto) {

        texto = texto.trim();


        if (!texto) {

            ocultarResultados();

            return;
        }


        try {

            const url =
                `/panel-administrador/productos/buscar/?q=${encodeURIComponent(texto)}`;


            const respuesta = await fetch(
                url,
                {
                    method: "GET",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                }
            );


            if (!respuesta.ok) {

                throw new Error(
                    "Error al buscar productos."
                );

            }


            const datos = await respuesta.json();


            mostrarResultados(
                datos.productos
            );


        } catch (error) {

            console.error(
                "Error en la búsqueda:",
                error
            );

            ocultarResultados();

        }

    }


    // =====================================================
    // ESCRIBIR EN EL BUSCADOR
    // =====================================================

    buscador.addEventListener(
        "input",
        function () {

            const texto =
                buscador.value.trim();


            clearTimeout(
                temporizador
            );


            if (!texto) {

                ocultarResultados();

                return;
            }


            temporizador = setTimeout(
                function () {

                    buscarProductos(
                        texto
                    );

                },
                250
            );

        }
    );


    // =====================================================
    // ABRIR PRODUCTO
    // =====================================================

    function abrirProducto(producto) {

        // -------------------------------------------------
        // ID
        // -------------------------------------------------

        const campoId =
            document.getElementById(
                "editar-producto-id"
            );

        if (campoId) {
            campoId.value =
                producto.id;
        }


        // -------------------------------------------------
        // NOMBRE
        // -------------------------------------------------

        const campoNombre =
            document.getElementById(
                "editar-nombre"
            );

        if (campoNombre) {
            campoNombre.value =
                producto.nombre;
        }


        // -------------------------------------------------
        // DESCRIPCIÓN
        // -------------------------------------------------

        const campoDescripcion =
            document.getElementById(
                "editar-descripcion"
            );

        if (campoDescripcion) {
            campoDescripcion.value =
                producto.descripcion;
        }


        // -------------------------------------------------
        // PRECIO
        // -------------------------------------------------

        const campoPrecio =
            document.getElementById(
                "editar-precio"
            );

        if (campoPrecio) {
            campoPrecio.value =
                producto.precio;
        }


        // -------------------------------------------------
        // STOCK
        // -------------------------------------------------

        const campoStock =
            document.getElementById(
                "editar-stock"
            );

        if (campoStock) {
            campoStock.value =
                producto.stock;
        }


        // -------------------------------------------------
        // ESTADO
        // -------------------------------------------------

        const campoEstado =
            document.getElementById(
                "editar-estado"
            );

        if (campoEstado) {
            campoEstado.value =
                producto.estado;
        }


        // -------------------------------------------------
        // CATEGORÍA
        // -------------------------------------------------

        const campoCategoria =
            document.getElementById(
                "editar-categoria"
            );

        if (campoCategoria) {
            campoCategoria.value =
                producto.categoria_id;
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
        // CERRAR RESULTADOS
        // -------------------------------------------------

        ocultarResultados();


        // -------------------------------------------------
        // ABRIR MODAL
        // -------------------------------------------------

        const modal =
            document.getElementById(
                "modal-editar-producto"
            );

        if (modal) {

            modal.classList.add(
                "mostrar"
            );

        }

    }


    // =====================================================
    // CLICK FUERA DEL BUSCADOR
    // =====================================================

    document.addEventListener(
        "click",
        function (evento) {

            const contenedor =
                document.querySelector(
                    ".productos-buscador-container"
                );


            if (
                contenedor &&
                !contenedor.contains(
                    evento.target
                )
            ) {

                ocultarResultados();

            }

        }
    );


    // =====================================================
    // ESC
    // =====================================================

    buscador.addEventListener(
        "keydown",
        function (evento) {

            if (evento.key === "Escape") {

                ocultarResultados();

                buscador.blur();

            }

        }
    );

});