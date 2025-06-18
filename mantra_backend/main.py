# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import productos, clientes, pedidos, detalles_pedido, categorias, imagenes_producto, carrito, cupones, reseñas, metodos_envio

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# CORS — permitir solicitudes desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar routers por módulo
app.include_router(productos.router)
app.include_router(clientes.router)
app.include_router(pedidos.router)
app.include_router(detalles_pedido.router)
app.include_router(categorias.router)
app.include_router(imagenes_producto.router)
app.include_router(carrito.router)
app.include_router(cupones.router)
app.include_router(reseñas.router)
app.include_router(metodos_envio.router)

# Ruta de bienvenida
@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Mantra Variedades"}
