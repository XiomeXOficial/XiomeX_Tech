const toasts = document.querySelectorAll(".toast");

toasts.forEach((toast) => {

    toast.style.animation = "toast-entrada .35s ease forwards";

    setTimeout(() => {

        toast.style.animation = "toast-salida .4s ease forwards";

        setTimeout(() => {

            toast.remove();

        }, 400);

    }, 3000);

});