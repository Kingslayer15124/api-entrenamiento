import sqlite3

DB_NAME = "app_entrenamiento.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entrenamientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            ejercicio TEXT NOT NULL,
            series INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            peso REAL NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    conexion.commit()
    conexion.close()