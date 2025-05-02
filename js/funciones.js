/*funcion para la marrquesina publicitaria */
const texto = document.getElementById("marquesina");
const btn = document.getElementById("toggleBtn");
let pausado = false;

btn.addEventListener("click", () => {
  pausado = !pausado;
  texto.style.animationPlayState = pausado ? "paused" : "running";
  btn.textContent = pausado ? "▶️" : "⏸️";
  btn.setAttribute(
    "aria-label",
    pausado ? "Reanudar marquesina" : "Pausar marquesina"
  );
});

/*funcion para el submenu de tenis en el menu general*/
document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelectorAll(".dropdown-submenu > a")
    .forEach(function (element) {
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

//funcion para el modal de presentacion
document.addEventListener("DOMContentLoaded", function () {
    const presentacionModal = new bootstrap.Modal(document.getElementById("presentacion"))
    presentacionModal.show()
  })

//funciones para el footer
document.getElementById("footer-year").textContent = new Date().getFullYear();
  
