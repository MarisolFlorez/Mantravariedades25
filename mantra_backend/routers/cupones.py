# routers/cupones.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import CuponOut, ValidarCuponIn
from datetime import datetime

router = APIRouter(prefix="/cupones", tags=["cupones"])

@router.get("/", response_model=List[CuponOut])
def listar_cupones():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cupones")
        cupones = cursor.fetchall()
        cursor.close()
        conn.close()
        return cupones
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/validar", response_model=CuponOut)
def validar_cupon(datos: ValidarCuponIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM cupones 
            WHERE codigo_cupon = %s 
              AND activo = TRUE 
              AND usos_actuales < usos_maximos 
              AND fecha_inicio <= %s 
              AND fecha_fin >= %s
            """,
            (datos.codigo_cupon, datetime.now(), datetime.now())
        )
        cupon = cursor.fetchone()
        cursor.close()
        conn.close()

        if not cupon:
            raise HTTPException(status_code=404, detail="Cupón inválido o expirado")

        return cupon

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
