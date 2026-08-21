const inputs = document.querySelectorAll(".codigo-input");

const codigoCompleto = document.getElementById(
    "codigo-completo"
);

const formulario = document.getElementById(
    "form-verificacion"
);


// =====================================================
// ACTUALIZAR CÓDIGO COMPLETO
// =====================================================

function actualizarCodigo() {

    let codigo = "";

    inputs.forEach((input) => {

        codigo += input.value;

    });

    codigoCompleto.value = codigo;
}


// =====================================================
// EVENTOS DE LOS INPUTS
// =====================================================

inputs.forEach((input, index) => {


    // =================================================
    // ESCRIBIR
    // =================================================

    input.addEventListener("input", () => {

        // Eliminar cualquier cosa que no sea número
        input.value = input.value.replace(/\D/g, "");


        actualizarCodigo();


        // Pasar automáticamente al siguiente
        if (
            input.value !== "" &&
            index < inputs.length - 1
        ) {

            inputs[index + 1].focus();

        }

    });


    // =================================================
    // TECLADO
    // =================================================

    input.addEventListener("keydown", (event) => {


        // Backspace
        if (
            event.key === "Backspace" &&
            input.value === "" &&
            index > 0
        ) {

            inputs[index - 1].focus();

        }


        // Flecha izquierda
        if (
            event.key === "ArrowLeft" &&
            index > 0
        ) {

            inputs[index - 1].focus();

        }


        // Flecha derecha
        if (
            event.key === "ArrowRight" &&
            index < inputs.length - 1
        ) {

            inputs[index + 1].focus();

        }

    });


    // =================================================
    // PEGAR
    // =================================================

    input.addEventListener("paste", (event) => {

        event.preventDefault();


        const texto = (
            event.clipboardData ||
            window.clipboardData
        ).getData("text");


        // Eliminar letras y símbolos
        const numeros = texto
            .replace(/\D/g, "")
            .slice(0, inputs.length);


        // Limpiar todos los campos
        inputs.forEach((campo) => {

            campo.value = "";

        });


        // Distribuir los números
        numeros
            .split("")
            .forEach((numero, i) => {

                inputs[i].value = numero;

            });


        actualizarCodigo();


        // Enfocar el último campo utilizado
        if (numeros.length > 0) {

            const posicion = Math.min(
                numeros.length,
                inputs.length - 1
            );

            inputs[posicion].focus();

        }

    });

});


// =====================================================
// ENVIAR FORMULARIO
// =====================================================

formulario.addEventListener("submit", (event) => {

    actualizarCodigo();


    // Deben existir exactamente 6 números
    if (codigoCompleto.value.length !== 6) {

        event.preventDefault();

        inputs[0].focus();

        return;

    }

});