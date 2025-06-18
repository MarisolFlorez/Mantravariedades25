# routers/categorias.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import CategoriaIn, CategoriaOut

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", response_model=List[CategoriaOut])
def listar_categorias():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        cursor.close()
        conn.close()
        return categorias
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: CategoriaIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO categorias (nombre_categoria, descripcion)
            VALUES (%s, %s)
            """,
            (categoria.nombre_categoria, categoria.descripcion)
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"mensaje": "Categoría creada exitosamente", "id_categoria": nuevo_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
