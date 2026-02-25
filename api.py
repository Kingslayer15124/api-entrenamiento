from fastapi import FastAPI
from database import crear_tablas
from usuarios import crear_usuario
from entrenamientos import crear_entrenamiento

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