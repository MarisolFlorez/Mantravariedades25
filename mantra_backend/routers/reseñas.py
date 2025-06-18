# routers/reseñas.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import ReseñaIn, ReseñaOut
from datetime import datetime

router = APIRouter(prefix="/reseñas", tags=["reseñas"])

@router.get("/", response_model=List[ReseñaOut])
def listar_reseñas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reseñas")
        reseñas = cursor.fetchall()
        cursor.close()
        conn.close()
        return reseñas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/producto/{id_producto}", response_model=List[ReseñaOut])
def reseñas_por_producto(id_producto: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reseñas WHERE id_producto = %s", (id_producto,))
        reseñas = cursor.fetchall()
        cursor.close()
        conn.close()
        return reseñas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_reseña(reseña: ReseñaIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO reseñas (id_producto, id_cliente, calificacion, comentario, fecha_reseña)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                reseña.id_producto,
                reseña.id_cliente,
                reseña.calificacion,
                reseña.comentario,
                datetime.now()
            )
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": "Reseña registrada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
