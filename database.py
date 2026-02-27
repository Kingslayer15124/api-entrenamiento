import sqlite3

usuarios_db = []
entrenamientos_db = []

def conectar():
    conexion = sqlite3.connect("entrenamiento.db")
    return conexion


def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        edad INTEGER,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entrenamientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        ejercicio TEXT,
        series INTEGER,
        reps INTEGER,
        peso REAL,
        fecha TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    """)

    conexion.commit()
    conexion.close()