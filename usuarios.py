from database import usuarios_db
from auth import hash_password, verify_password


def crear_usuario(nombre, edad, password):
    for usuario in usuarios_db:
        if usuario["nombre"] == nombre:
            return {"error": "El usuario ya existe"}

    password_hash = hash_password(password)

    nuevo_usuario = {
        "nombre": nombre,
        "edad": edad,
        "password": password_hash
    }

    usuarios_db.append(nuevo_usuario)

    return {"mensaje": "Usuario creado correctamente"}


def buscar_usuario(nombre):
    for usuario in usuarios_db:
        if usuario["nombre"] == nombre:
            return usuario
    return None


def autenticar_usuario(nombre, password):
    usuario = buscar_usuario(nombre)

    if not usuario:
        return None

    if not verify_password(password, usuario["password"]):
        return None

    return usuario