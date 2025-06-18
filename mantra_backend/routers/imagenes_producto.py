# routers/imagenes_producto.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import ImagenProductoIn, ImagenProductoOut

router = APIRouter(prefix="/imagenes-producto", tags=["imagenes_producto"])

@router.get("/producto/{id_producto}", response_model=List[ImagenProductoOut])
def listar_imagenes_por_producto(id_producto: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM imagenes_producto WHERE id_producto = %s ORDER BY orden ASC",
            (id_producto,)
        )
        imagenes = cursor.fetchall()
        cursor.close()
        conn.close()
        return imagenes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=status.HTTP_201_CREATED)
def agregar_imagen(imagen: ImagenProductoIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO imagenes_producto (id_producto, url_imagen, orden)
            VALUES (%s, %s, %s)
            """,
            (imagen.id_producto, imagen.url_imagen, imagen.orden)
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Imagen agregada exitosamente", "id_imagen": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
