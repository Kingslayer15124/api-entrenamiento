from database import conectar
from datetime import datetime

def crear_entrenamiento(usuario_id, ejercicio, series, reps, peso):

    conexion = conectar()
    cursor = conexion.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    cursor.execute("""
        INSERT INTO entrenamientos
        (usuario_id, ejercicio, series, reps, peso, fecha)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (usuario_id, ejercicio, series, reps, peso, fecha))

    conexion.commit()
    conexion.close()

    return {"mensaje": "Entrenamiento registrado"}