from database import conectar
from datetime import datetime


def crear_entrenamiento_autenticado(nombre_usuario, ejercicio, series, reps, peso):

    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener ID del usuario a partir del nombre
    cursor.execute(
        "SELECT id FROM usuarios WHERE nombre = ?",
        (nombre_usuario,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        conexion.close()
        return {"error": "Usuario no encontrado"}

    usuario_id = resultado[0]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute("""
        INSERT INTO entrenamientos
        (usuario_id, ejercicio, series, reps, peso, fecha)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario_id, ejercicio, series, reps, peso, fecha))

    conexion.commit()
    conexion.close()

    return {"mensaje": "Entrenamiento registrado correctamente"}