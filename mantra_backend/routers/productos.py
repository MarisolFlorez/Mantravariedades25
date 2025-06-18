# routers/productos.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import ProductoIn, ProductoOut

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/", response_model=List[ProductoOut])
def listar_productos():
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM productos")
                productos = cursor.fetchall()
        return productos
    except Exception:
        raise HTTPException(status_code=500, detail="Error al obtener productos")

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO productos
              (nombre_producto, descripcion, precio, stock, id_categoria, url_imagen_principal)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                producto.nombre_producto,
                producto.descripcion,
                producto.precio,
                producto.stock,
                producto.id_categoria,
                producto.url_imagen_principal
            )
        )
        conn.commit()
        producto_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Producto creado exitosamente", "id": producto_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
