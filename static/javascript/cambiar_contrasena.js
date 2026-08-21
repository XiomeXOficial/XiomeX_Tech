document.addEventListener("DOMContentLoaded", function () {

    const botones = document.querySelectorAll(".mostrar-password");

    botones.forEach(function (boton) {

        boton.addEventListener("click", function () {

            const inputId = boton.dataset.target;
            const input = document.getElementById(inputId);
            const icono = boton.querySelector("i");

            if (input.type === "password") {

                input.type = "text";

                icono.classList.remove("fa-eye");
                icono.classList.add("fa-eye-slash");

                boton.setAttribute(
                    "aria-label",
                    "Ocultar contraseña"
                );

            } else {

                input.type = "password";

                icono.classList.remove("fa-eye-slash");
                icono.classList.add("fa-eye");

                boton.setAttribute(
                    "aria-label",
                    "Mostrar contraseña"
                );

            }

        });

    });

});