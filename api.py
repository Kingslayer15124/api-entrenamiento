from fastapi import FastAPI, Depends
from database import crear_tablas
from usuarios import crear_usuario, login
from entrenamientos import crear_entrenamiento_autenticado
from auth import verificar_token

app = FastAPI()

crear_tablas()


@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}


@app.post("/registro/")
def api_registro(nombre: str, edad: int, password: str):
    return crear_usuario(nombre, edad, password)


@app.post("/login/")
def api_login(nombre: str, password: str):
    return login(nombre, password)


@app.get("/protegido/")
def ruta_protegida(usuario: str = Depends(verificar_token)):
    return {"mensaje": f"Hola {usuario}, estás autenticado"}


@app.post("/entrenamientos/")
def api_crear_entrenamiento(
    ejercicio: str,
    series: int,
    reps: int,
    peso: float,
    usuario: str = Depends(verificar_token)
):
    return crear_entrenamiento_autenticado(
        usuario, ejercicio, series, reps, peso
    )