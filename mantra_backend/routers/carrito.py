from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import CarritoIn, CarritoOut
from datetime import datetime

router = APIRouter(prefix="/carrito", tags=["carrito"])

@router.get("/{id_cliente}", response_model=List[CarritoOut])
def obtener_carrito(id_cliente: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM carrito WHERE id_cliente = %s", (id_cliente,)
        )
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=status.HTTP_201_CREATED)
def agregar_al_carrito(item: CarritoIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        now = datetime.now()

        # Verificar si el producto ya está en el carrito
        cursor.execute(
            "SELECT * FROM carrito WHERE id_cliente = %s AND id_producto = %s",
            (item.id_cliente, item.id_producto)
        )
        existente = cursor.fetchone()

        if existente:
            # Actualizar cantidad y última actualización
            cursor.execute(
                """
                UPDATE carrito SET cantidad = cantidad + %s, ultima_actualizacion = %s
                WHERE id_cliente = %s AND id_producto = %s
                """,
                (item.cantidad, now, item.id_cliente, item.id_producto)
            )
        else:
            # Insertar nuevo ítem
            cursor.execute(
                """
                INSERT INTO carrito (id_cliente, id_producto, cantidad, fecha_creacion, ultima_actualizacion)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (item.id_cliente, item.id_producto, item.cantidad, now, now)
            )

        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": "Producto agregado al carrito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id_cliente}/{id_producto}")
def eliminar_producto_carrito(id_cliente: int, id_producto: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM carrito WHERE id_cliente = %s AND id_producto = %s",
            (id_cliente, id_producto)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": "Producto eliminado del carrito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
