from database import conectar

def crear_usuario(nombre, edad):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
        (nombre, edad)
    )

    conexion.commit()
    conexion.close()

    return {"mensaje": "Usuario creado"}