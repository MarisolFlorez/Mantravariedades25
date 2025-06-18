# routers/detalles_pedido.py
from fastapi import APIRouter, HTTPException, status, Path
from typing import List
from db import get_db_connection
from schemas import DetallePedidoIn, DetallePedidoOut

router = APIRouter(prefix="/detalles_pedido", tags=["detalles_pedido"])

# Listar todos los detalles de pedidos
@router.get("/", response_model=List[DetallePedidoOut])
def listar_detalles_pedidos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_pedido")
        detalles = cursor.fetchall()
        cursor.close()
        conn.close()
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Listar detalles por id_pedido
@router.get("/{id_pedido}", response_model=List[DetallePedidoOut])
def obtener_detalles_por_pedido(id_pedido: int = Path(..., description="ID del pedido")):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM detalles_pedido WHERE id_pedido = %s", (id_pedido,))
        detalles = cursor.fetchall()
        cursor.close()
        conn.close()
        if not detalles:
            raise HTTPException(status_code=404, detail="No se encontraron detalles para este pedido")
        return detalles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear nuevo detalle de pedido
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_detalle_pedido(detalle: DetallePedidoIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, %s)
            """,
            (
                detalle.id_pedido,
                detalle.id_producto,
                detalle.cantidad,
                detalle.precio_unitario
            )
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Detalle de pedido creado exitosamente", "id_detalle": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
