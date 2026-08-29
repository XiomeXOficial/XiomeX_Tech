document.addEventListener("DOMContentLoaded", function () {

    const botonesEliminar = document.querySelectorAll(".usuario-eliminar");

    botonesEliminar.forEach(function (boton) {

        boton.addEventListener("click", function (event) {

            event.preventDefault();

            const nombre = boton.dataset.usuario;
            const url = boton.href;

            mostrarConfirmacion(nombre, url);

        });

    });

});


function mostrarConfirmacion(nombre, url) {

    const overlay = document.createElement("div");

    overlay.className = "confirmacion-overlay";

    overlay.innerHTML = `
        <div class="confirmacion-modal">

            <div class="confirmacion-icono">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>

            <h2>¿Estás seguro?</h2>

            <p>
                ¿Estás seguro de que quieres eliminar a
                <strong>${nombre}</strong>?
            </p>

            <p class="confirmacion-advertencia">
                Esta acción no se puede deshacer.
            </p>

            <div class="confirmacion-botones">

                <button
                    type="button"
                    class="confirmacion-cancelar"
                    id="cancelar-eliminacion"
                >
                    Cancelar
                </button>

                <button
                    type="button"
                    class="confirmacion-eliminar"
                    id="confirmar-eliminacion"
                >
                    Eliminar
                </button>

            </div>

        </div>
    `;

    document.body.appendChild(overlay);

    requestAnimationFrame(function () {
        overlay.classList.add("mostrar");
    });


    document
        .getElementById("cancelar-eliminacion")
        .addEventListener("click", function () {

            cerrarConfirmacion(overlay);

        });


    document
        .getElementById("confirmar-eliminacion")
        .addEventListener("click", function () {

            window.location.href = url;

        });


    overlay.addEventListener("click", function (event) {

        if (event.target === overlay) {

            cerrarConfirmacion(overlay);

        }

    });

}


function cerrarConfirmacion(overlay) {

    overlay.classList.remove("mostrar");

    setTimeout(function () {

        overlay.remove();

    }, 250);

}

    // =====================================================
    // BUSCADOR DE PRODUCTOS
    // =====================================================

    const buscadorProducto =
        document.getElementById("buscar-producto");

    const filasProductos =
        document.querySelectorAll("#productos-body tr");

    const sinResultadosProductos =
        document.getElementById("sin-resultados-productos");

    const contadorProductos =
        document.getElementById("contador-productos");


    if (buscadorProducto) {

        buscadorProducto.addEventListener(
            "input",
            function () {

                const texto = this.value
                    .toLowerCase()
                    .trim();

                let encontrados = 0;


                filasProductos.forEach(
                    function (fila) {

                        const contenido =
                            fila.textContent.toLowerCase();


                        if (contenido.includes(texto)) {

                            fila.style.display = "";

                            encontrados++;

                        } else {

                            fila.style.display = "none";

                        }

                    }
                );


                // ---------------------------------------------
                // MOSTRAR / OCULTAR MENSAJE
                // ---------------------------------------------

                if (
                    texto !== "" &&
                    encontrados === 0
                ) {

                    sinResultadosProductos.style.display =
                        "block";

                } else {

                    sinResultadosProductos.style.display =
                        "none";

                }


                // ---------------------------------------------
                // ACTUALIZAR CONTADOR
                // ---------------------------------------------

                contadorProductos.textContent =
                    encontrados;

            }
        );

    }