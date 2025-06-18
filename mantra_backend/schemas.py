# schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# -----------------------
# Modelos de entrada (POST)
# -----------------------

class ProductoIn(BaseModel):
    nombre_producto: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    id_categoria: int
    url_imagen_principal: Optional[str] = None

class ClienteIn(BaseModel):
    nombre: str
    apellido: str
    email: str
    contraseña: str
    direccion: str
    ciudad: str
    codigo_postal: str
    pais: str
    telefono: str

class LoginIn(BaseModel):
    email: str
    contraseña: str

class PedidoIn(BaseModel):
    id_cliente: int
    direccion_envio: str
    ciudad_envio: str
    codigo_postal_envio: str
    pais_envio: str
    metodo_pago: str
    total_pedido: float
    fecha_pedido: Optional[datetime] = None  # Se puede generar en el backend

class DetallePedidoIn(BaseModel):
    id_pedido: int
    id_producto: int
    cantidad: int
    precio_unitario: float

# -----------------------
# Modelo de salida (response)
# Producto
class ProductoOut(BaseModel):
    id_producto: int
    nombre_producto: str
    descripcion: Optional[str]
    precio: float
    stock: int
    id_categoria: int
    url_imagen_principal: Optional[str]

# Cliente
class ClienteOut(BaseModel):
    id_cliente: int
    nombre: str
    apellido: str
    email: str
    direccion: str
    ciudad: str
    codigo_postal: str
    pais: str
    telefono: str

# Pedido
class PedidoOut(BaseModel):
    id_pedido: int
    id_cliente: int
    fecha_pedido: datetime
    estado_pedido: str
    total_pedido: float
    direccion_envio: str
    ciudad_envio: str
    codigo_postal_envio: str
    pais_envio: str
    metodo_pago: str

# DetallePedido
class DetallePedidoOut(BaseModel):
    id_detalle: int
    id_pedido: int
    id_producto: int
    cantidad: int
    precio_unitario: float

# Categoría
class CategoriaIn(BaseModel):
    nombre_categoria: str
    descripcion: Optional[str] = None

class CategoriaOut(BaseModel):
    id_categoria: int
    nombre_categoria: str
    descripcion: Optional[str]

# Imágenes de producto
class ImagenProductoIn(BaseModel):
    id_producto: int
    url_imagen: str
    orden: int

class ImagenProductoOut(BaseModel):
    id_imagen: int
    id_producto: int
    url_imagen: str
    orden: int

# Carrito

from datetime import datetime

class CarritoIn(BaseModel):
    id_cliente: int
    id_producto: int
    cantidad: int

class CarritoOut(BaseModel):
    id_carrito: int
    id_cliente: int
    id_producto: int
    cantidad: int
    fecha_creacion: datetime
    ultima_actualizacion: datetime

# Cupones

class CuponOut(BaseModel):
    id_cupon: int
    codigo_cupon: str
    tipo_descuento: str  # ejemplo: "porcentaje" o "monto_fijo"
    valor_descuento: float
    fecha_inicio: datetime
    fecha_fin: datetime
    usos_maximos: int
    usos_actuales: int
    activo: bool

class ValidarCuponIn(BaseModel):
    codigo_cupon: str

# Reseñas

class ReseñaIn(BaseModel):
    id_producto: int
    id_cliente: int
    calificacion: int  # Por ejemplo: de 1 a 5
    comentario: str

class ReseñaOut(BaseModel):
    id_reseña: int
    id_producto: int
    id_cliente: int
    calificacion: int
    comentario: str
    fecha_reseña: datetime

# Métodos de envío

class MetodoEnvioIn(BaseModel):
    nombre_metodo: str
    costo: float
    descripcion: Optional[str] = None

class MetodoEnvioOut(BaseModel):
    id_metodo_envio: int
    nombre_metodo: str
    costo: float
    descripcion: Optional[str]








