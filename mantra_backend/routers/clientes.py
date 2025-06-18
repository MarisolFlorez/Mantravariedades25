# routers/clientes.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from db import get_db_connection
from schemas import ClienteIn, ClienteOut, LoginIn

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.get("/", response_model=List[ClienteOut])
def listar_clientes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        for cliente in clientes:
            cliente.pop("contraseña", None)  # No exponer contraseñas
        cursor.close()
        conn.close()
        return clientes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: ClienteIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Verificar si el email ya está registrado
        cursor.execute("SELECT id_cliente FROM clientes WHERE email = %s", (cliente.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="El correo ya está registrado")

        # Insertar nuevo cliente
        cursor.execute(
            """
            INSERT INTO clientes 
              (nombre, apellido, email, contraseña, direccion, ciudad, codigo_postal, pais, telefono)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                cliente.nombre,
                cliente.apellido,
                cliente.email,
                cliente.contraseña,
                cliente.direccion,
                cliente.ciudad,
                cliente.codigo_postal,
                cliente.pais,
                cliente.telefono
            )
        )
        nuevo_id = cursor.lastrowid
        conn.commit()

        # Obtener cliente recién creado (sin contraseña)
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (nuevo_id,))
        cliente_creado = cursor.fetchone()
        cliente_creado.pop("contraseña", None)

        cursor.close()
        conn.close()
        return cliente_creado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login")
def login_cliente(datos: LoginIn):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM clientes WHERE email = %s AND contraseña = %s",
            (datos.email, datos.contraseña)
        )
        cliente = cursor.fetchone()
        cursor.close()
        conn.close()

        if cliente:
            cliente.pop("contraseña", None)
            return {"mensaje": "Login exitoso", "cliente": cliente}
        else:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
