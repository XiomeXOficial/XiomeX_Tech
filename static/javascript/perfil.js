const correo = document.getElementById("correo");
const botonCorreo = document.getElementById("mostrar-correo");
const correoOriginal = correo.textContent.trim();

let correoVisible = false;

function ocultarCorreo(correo) {
    const partes = correo.split("@");
    const nombre = partes[0];
    const dominio = partes[1];

    if (nombre.length <= 2) {
        return "*".repeat(nombre.length) + "@" + dominio;
    }

    return nombre[0] + "*".repeat(nombre.length - 1) + "@" + dominio;
}

correo.textContent = ocultarCorreo(correoOriginal);

botonCorreo.addEventListener("click", function() {
    correoVisible = !correoVisible;

    if (correoVisible) {
        correo.textContent = correoOriginal;
        botonCorreo.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
    } else {
        correo.textContent = ocultarCorreo(correoOriginal);
        botonCorreo.innerHTML = '<i class="fa-solid fa-eye"></i>';
    }
});

document.getElementById("foto-input").addEventListener("change", function() {
    if (this.files.length > 0) {
        document.getElementById("foto-form").submit();
    }
});