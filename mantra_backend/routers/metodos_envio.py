# routers/metodos_envio.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import MetodoEnvioIn, MetodoEnvioOut

router = APIRouter(prefix="/metodos-envio", tags=["metodos_envio"])

@router.get("/", response_model=List[MetodoEnvioOut])
def listar_metodos_envio():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM metodos_envio")
        metodos = cursor.fetchall()
        cursor.close()
        conn.close()
        return metodos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_metodo_envio(metodo: MetodoEnvioIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO metodos_envio (nombre_metodo, costo, descripcion)
            VALUES (%s, %s, %s)
            """,
            (
                metodo.nombre_metodo,
                metodo.costo,
                metodo.descripcion
            )
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Método de envío creado exitosamente", "id_metodo_envio": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
