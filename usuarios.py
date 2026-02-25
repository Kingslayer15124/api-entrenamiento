from database import conectar
import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verificar_password(password: str, hashed: str):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed.encode('utf-8')
    )

def crear_usuario(nombre, edad, password):

    conexion = conectar()
    cursor = conexion.cursor()

    password_hash = hash_password(password)

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

    if verificar_password(password, password_guardada):
        return {"mensaje": "Login exitoso"}
    else:
        return {"error": "Contraseña incorrecta"}