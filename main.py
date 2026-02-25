from database import crear_tablas
from usuarios import crear_usuario
from entrenamientos import crear_entrenamiento

def menu():
    crear_tablas()

    while True:
        print("\n1. Agregar usuario")
        print("2. Registrar entrenamiento")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            crear_usuario(nombre, edad)
            print("Usuario creado.")

        elif opcion == "2":
            usuario_id = int(input("ID usuario: "))
            ejercicio = input("Ejercicio: ")
            series = int(input("Series: "))
            reps = int(input("Reps: "))
            peso = float(input("Peso: "))

            crear_entrenamiento(usuario_id, ejercicio, series, reps, peso)
            print("Entrenamiento registrado.")

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()