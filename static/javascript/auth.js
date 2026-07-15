const authPanel = document.getElementById("auth-panel");

const registerButton = document.getElementById("show-register");
const loginButton = document.getElementById("show-login");

// Si viene desde "Registrarse"

const params = new URLSearchParams(window.location.search);

if (params.get("mode") === "register"){

    authPanel.classList.add("active");

}

registerButton.addEventListener("click", () => {

    authPanel.classList.add("active");

});

loginButton.addEventListener("click", () => {

    authPanel.classList.remove("active");

});