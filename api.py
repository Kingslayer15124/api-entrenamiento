from fastapi import FastAPI
from database import crear_tablas
from usuarios import crear_usuario
from entrenamientos import crear_entrenamiento
from usuarios import crear_usuario, login

app = FastAPI()

crear_tablas()


@app.get("/")
def root():
    return {"mensaje": "API Entrenamiento funcionando"}


@app.post("/usuarios/")
def api_crear_usuario(nombre: str, edad: int):
    return crear_usuario(nombre, edad)


@app.post("/entrenamientos/")
def api_crear_entrenamiento(
    usuario_id: int,
    ejercicio: str,
    series: int,
    reps: int,
    peso: float
):
    return crear_entrenamiento(usuario_id, ejercicio, series, reps, peso)

@app.post("/registro/")
def api_registro(nombre: str, edad: int, password: str):
    return crear_usuario(nombre, edad, password)


@app.post("/login/")
def api_login(nombre: str, password: str):
    return login(nombre, password)