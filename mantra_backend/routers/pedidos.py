# routers/pedidos.py
from fastapi import APIRouter, HTTPException, status, Query, Path
from typing import List, Optional
from db import get_db_connection
from schemas import PedidoIn, PedidoOut

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

# Listar pedidos (opcionalmente filtrado por cliente)
@router.get("/", response_model=List[PedidoOut])
def listar_pedidos(id_cliente: Optional[int] = Query(None)):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        if id_cliente is not None:
            cursor.execute("SELECT * FROM pedidos WHERE id_cliente = %s", (id_cliente,))
        else:
            cursor.execute("SELECT * FROM pedidos")

        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear nuevo pedido
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pedido(pedido: PedidoIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO pedidos
              (id_cliente, fecha_pedido, estado_pedido, total_pedido,
               direccion_envio, ciudad_envio, codigo_postal_envio, pais_envio, metodo_pago)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                pedido.id_cliente,
                pedido.fecha_pedido or None,  # puede ser None y manejarse con valor por defecto en BD
                "Pendiente",  # estado inicial fijo
                pedido.total_pedido,
                pedido.direccion_envio,
                pedido.ciudad_envio,
                pedido.codigo_postal_envio,
                pedido.pais_envio,
                pedido.metodo_pago
            )
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Pedido creado exitosamente", "id_pedido": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Actualizar el estado de un pedido
@router.put("/{id_pedido}/estado")
def actualizar_estado_pedido(
    id_pedido: int = Path(..., description="ID del pedido a actualizar"),
    nuevo_estado: str = Query(..., description="Nuevo estado del pedido")
):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE pedidos SET estado_pedido = %s WHERE id_pedido = %s",
            (nuevo_estado, id_pedido)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": f"Estado del pedido {id_pedido} actualizado a '{nuevo_estado}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
