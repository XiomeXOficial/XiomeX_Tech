document.addEventListener("DOMContentLoaded", function () {


    // =====================================================
    // ELEMENTOS
    // =====================================================

    const modalCrear =
        document.getElementById("modal-crear");

    const modalEditar =
        document.getElementById("modal-editar");

    const modalEliminar =
        document.getElementById("modal-eliminar");


    const abrirCrear =
        document.getElementById("abrir-crear-categoria");


    const botonesEditar =
        document.querySelectorAll(".categoria-editar");


    const botonesEliminar =
        document.querySelectorAll(".categoria-eliminar");


    const botonesCerrar =
        document.querySelectorAll("[data-cerrar]");


    // =====================================================
    // ABRIR CREAR
    // =====================================================

    abrirCrear.addEventListener("click", function () {

        modalCrear.classList.add("mostrar");

        document
            .getElementById("nombre-crear")
            .focus();

    });


    // =====================================================
    // EDITAR
    // =====================================================

    botonesEditar.forEach(function (boton) {

        boton.addEventListener("click", function () {

            const id =
                boton.dataset.id;

            const nombre =
                boton.dataset.nombre;


            document
                .getElementById("editar-categoria-id")
                .value = id;


            document
                .getElementById("nombre-editar")
                .value = nombre;


            modalEditar.classList.add("mostrar");


            document
                .getElementById("nombre-editar")
                .focus();

        });

    });


    // =====================================================
    // ELIMINAR
    // =====================================================

    botonesEliminar.forEach(function (boton) {

        boton.addEventListener("click", function () {

            const id =
                boton.dataset.id;

            const nombre =
                boton.dataset.nombre;


            document
                .getElementById("eliminar-categoria-id")
                .value = id;


            document
                .getElementById("eliminar-categoria-nombre")
                .textContent =
                nombre;


            modalEliminar.classList.add("mostrar");

        });

    });


    // =====================================================
    // CERRAR
    // =====================================================

    botonesCerrar.forEach(function (boton) {

        boton.addEventListener("click", function () {

            const idModal =
                boton.dataset.cerrar;

            cerrarModal(idModal);

        });

    });


    // =====================================================
    // CERRAR HACIENDO CLICK FUERA
    // =====================================================

    [modalCrear, modalEditar, modalEliminar]
        .forEach(function (modal) {

            modal.addEventListener(
                "click",
                function (event) {

                    if (
                        event.target === modal
                    ) {

                        modal.classList.remove(
                            "mostrar"
                        );

                    }

                }
            );

        });


    // =====================================================
    // ESC
    // =====================================================

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key === "Escape") {

                [modalCrear, modalEditar, modalEliminar]
                    .forEach(function (modal) {

                        modal.classList.remove(
                            "mostrar"
                        );

                    });

            }

        }
    );

});


function cerrarModal(id) {

    const modal =
        document.getElementById(id);


    if (modal) {

        modal.classList.remove(
            "mostrar"
        );

    }

}