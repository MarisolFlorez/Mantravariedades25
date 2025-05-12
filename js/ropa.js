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

//funcion para mostrar productos por categoria
// Lista de productos
const productos = [
  {
    nombre: "Blusa floral mujer",
    precio: 49900,
    categoria: "femenina",
    imagen: "/Imagenes/ImagenesRopa/femenina/femeninaPrueba.jpg"
  },
  {
    nombre: "Camisa casual hombre",
    precio: 59900,
    categoria: "masculina",
    imagen: "/Imagenes/ImagenesRopa/masculina/masculinaPrueba.jpg"
  },
  {
    nombre: "Sudadera urbana",
    precio: 72900,
    categoria: "urbana",
    imagen: "/Imagenes/ImagenesRopa/urbana/urbanaPrueba.jpg"
  },
  {
    nombre: "Set infantil personajes",
    precio: 39900,
    categoria: "infantil",
    imagen: "/Imagenes/ImagenesRopa/infantil/infantilPrueba.jpg"
  }
];

// Función para mostrar productos según categoría
function mostrarProductos(categoriaSeleccionada) {
  const contenedor = document.getElementById("productos-container");
  contenedor.innerHTML = "";

  const filtrados = productos.filter(p => p.categoria === categoriaSeleccionada);

  filtrados.forEach((producto, index) => {
    const card = document.createElement("div");
    card.className = "col-6 col-md-4 col-lg-3 mb-4";

    card.innerHTML = `
      <div class="card h-100 producto-card" style="animation-delay: ${index * 100}ms">
        <img src="${producto.imagen}" class="card-img-top" alt="${producto.nombre}">
        <div class="card-body">
          <h6 class="card-title">${producto.nombre}</h6>
          <p class="card-text">$${producto.precio.toLocaleString()}</p>
          <button class="btn btn-sm btn-primary">Agregar al carrito</button>
        </div>
      </div>
    `;

    contenedor.appendChild(card);
  });
}

// Escuchar cambios en los radios de categoría
document.querySelectorAll('input[name="categoria"]').forEach(radio => {
  radio.addEventListener("change", () => {
    const categoria = radio.id.replace("cat-", "");
    mostrarProductos(categoria);
  });
});

// Mostrar categoría inicial
mostrarProductos("femenina");

// Desplegar submenús en navbar (opcional si lo usas)
document.querySelectorAll('.dropdown-submenu > a').forEach(function(element) {
  element.addEventListener('click', function(e) {
    const nextEl = this.nextElementSibling;
    if (nextEl && nextEl.classList.contains('dropdown-menu')) {
      e.preventDefault();
      e.stopPropagation();
      nextEl.classList.toggle('show');
    }
  });
});


//funcion para que productos en el menu despliegue a la Izq
document.querySelectorAll(".dropdown-submenu > a").forEach(function (element) {
  element.addEventListener("click", function (e) {
    const nextEl = this.nextElementSibling;
    if (nextEl && nextEl.classList.contains("dropdown-menu")) {
      e.preventDefault();
      e.stopPropagation();
      nextEl.classList.toggle("show");
    }
  });
});
