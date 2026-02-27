from database import conectar
from passlib.context import CryptContext
from auth import crear_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crear_usuario(nombre, edad, password):

    conexion = conectar()
    cursor = conexion.cursor()

    password_hash = pwd_context.hash(password)

    cursor.execute(
        "INSERT INTO usuarios (nombre, edad, password) VALUES (?, ?, ?)",
        (nombre, edad, password_hash)
    )

    conexion.commit()
    conexion.close()

    return {"mensaje": "Usuario creado correctamente"}


def login(nombre, password):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT password FROM usuarios WHERE nombre = ?",
        (nombre,)
    )

    resultado = cursor.fetchone()
    conexion.close()

    if resultado is None:
        return {"error": "Usuario no encontrado"}

    password_guardada = resultado[0]

    if pwd_context.verify(password, password_guardada):
        access_token = crear_token(data={"sub": nombre})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        return {"error": "Contraseña incorrecta"}