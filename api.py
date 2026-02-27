# api.py

from fastapi import FastAPI, HTTPException
from usuarios import crear_usuario, autenticar_usuario
from entrenamientos import crear_entrenamiento, obtener_entrenamientos
from auth import create_access_token

app = FastAPI()


@app.post("/registro/")
def api_registro(nombre: str, edad: int, password: str):
    resultado = crear_usuario(nombre, edad, password)

    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])

    return resultado


@app.post("/login/")
def api_login(nombre: str, password: str):
    usuario = autenticar_usuario(nombre, password)

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": usuario["nombre"]})

    return {"access_token": access_token}


@app.post("/entrenamientos/")
def api_crear_entrenamiento(nombre_usuario: str, descripcion: str):
    return crear_entrenamiento(nombre_usuario, descripcion)


@app.get("/entrenamientos/")
def api_obtener_entrenamientos():
    return obtener_entrenamientos()