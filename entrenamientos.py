from database import entrenamientos_db


def crear_entrenamiento(nombre_usuario, descripcion):
    nuevo_entrenamiento = {
        "usuario": nombre_usuario,
        "descripcion": descripcion
    }

    entrenamientos_db.append(nuevo_entrenamiento)

    return {"mensaje": "Entrenamiento creado"}


def obtener_entrenamientos():
    return entrenamientos_db