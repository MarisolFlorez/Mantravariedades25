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

//funcion para barra de busqueda
// Lista de productos base (puedes reemplazarla por datos reales del backend más adelante)
const productos = [
  "Zapatos deportivos",
  "Blusas dama estampadas",
  "Camisas caballero manga larga",
  "Calzado infantil para niñas",
  "Calzado infantil para niños",
  "Relojes de pulsera",
  "Gorras planas",
  "Bolsos de cuero",
  "Bolsos casuales",
  "Zapatos formales",
  "Blusas dama sin mangas",
  "Camisas caballero casuales"
];

const searchInput = document.getElementById("search-input");
const suggestionsContainer = document.getElementById("search-suggestions");

// Escucha los cambios en el input
searchInput.addEventListener("input", () => {
  const query = searchInput.value.toLowerCase().trim();
  suggestionsContainer.innerHTML = ""; // Limpia sugerencias previas

  if (query === "") return;

  const resultados = productos.filter(producto =>
    producto.toLowerCase().includes(query)
  );

  if (resultados.length === 0) {
    suggestionsContainer.innerHTML = "<div class='no-result'>No se encontraron resultados.</div>";
    return;
  }

  resultados.forEach(producto => {
    const item = document.createElement("div");
    item.classList.add("suggestion-item");
    item.textContent = producto;
    item.addEventListener("click", () => {
      searchInput.value = producto;
      suggestionsContainer.innerHTML = "";
      // Aquí podrías redirigir o mostrar los productos filtrados, por ejemplo:
      console.log("Buscar producto:", producto);
    });
    suggestionsContainer.appendChild(item);
  });
});


//funcion para las reseñas creativas
function scrollTestimonios(direction) {
  const container = document.querySelector(".scroll-container");
  const cardWidth = 300 + 24; // Ancho de tarjeta + espacio entre tarjetas
  container.scrollBy({ left: direction * cardWidth, behavior: "smooth" });
}

//funciones para el footer
document.getElementById("footer-year").textContent = new Date().getFullYear();