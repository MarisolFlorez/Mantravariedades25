//funcion de la marquesina publicitaria
document.addEventListener("DOMContentLoaded", function () {
    const marquesina = document.getElementById("marquesina");
    const toggleBtn = document.getElementById("toggleBtn");

    let isPaused = false;

    toggleBtn.addEventListener("click", function () {
        if (isPaused) {
            marquesina.style.animationPlayState = "running";
            toggleBtn.innerText = "⏸️";
        } else {
            marquesina.style.animationPlayState = "paused";
            toggleBtn.innerText = "▶️";
        }
        isPaused = !isPaused;
    });
});

/*funcion para el submenu de tenis en el menu general*/
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".dropdown-submenu > a").forEach(function (element) {
        element.addEventListener("click", function (e) {
            const submenu = this.nextElementSibling;
            if (submenu && submenu.classList.contains("dropdown-menu")) {
                e.preventDefault();
                submenu.classList.toggle("show");
            }
        });
    });

    // Cierra submenús al cerrar dropdown principal
    document.querySelectorAll(".dropdown").forEach(function (dropdown) {
        dropdown.addEventListener("hide.bs.dropdown", function () {
            this.querySelectorAll(".dropdown-menu.show").forEach(function (submenu) {
                submenu.classList.remove("show");
            });
        });
    });
});



