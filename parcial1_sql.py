import sqlite3
import os

# Función para conectar a la base de datos
def conectar_bd():
    conexion = sqlite3.connect("tienda_autos.db")
    return conexion

# Función para crear la tabla si no existe
def inicializar_bd():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            marca TEXT NOT NULL,
            precio INTEGER NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()

# Función para agregar un auto al inventario
def agregar_auto(modelo, marca, precio):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO autos (modelo, marca, precio) VALUES (?, ?, ?)", (modelo, marca, precio))

    conexion.commit()
    conexion.close()

# Función para buscar un auto por modelo
def buscar_auto(modelo):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM autos WHERE modelo=?", (modelo,))
    resultado = cursor.fetchone()

    conexion.close()

    return resultado

# Función para listar todos los autos en el inventario
def listar_autos():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM autos")
    resultados = cursor.fetchall()

    conexion.close()

    return resultados

# Función para actualizar el precio de un auto
def actualizar_precio(id_auto, nuevo_precio):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("UPDATE autos SET precio=? WHERE id=?", (nuevo_precio, id_auto))

    conexion.commit()
    conexion.close()

# Función para eliminar un auto por ID
def eliminar_auto(id_auto):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM autos WHERE id=?", (id_auto,))

    conexion.commit()
    conexion.close()

# Función principal del programa
def main():
    inicializar_bd()

    while True:
        print("\n=== Tienda de Autos ===")
        print("1. Agregar auto")
        print("2. Buscar auto")
        print("3. Listar autos")
        print("4. Actualizar precio")
        print("5. Eliminar auto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            modelo = input("Ingrese el modelo del auto: ")
            marca = input("Ingrese la marca del auto: ")
            precio = int(input("Ingrese el precio: "))
            agregar_auto(modelo, marca, precio)
            print("Auto agregado correctamente.")

        elif opcion == "2":
            modelo = input("Ingrese el modelo del auto a buscar: ")
            resultado = buscar_auto(modelo)
            if resultado:
                print(f"ID: {resultado[0]}, Modelo: {resultado[1]}, Marca: {resultado[2]}, Precio: {resultado[3]}")
            else:
                print("Auto no encontrado.")

        elif opcion == "3":
            resultados = listar_autos()
            if resultados:
                print("\n=== Autos en la tienda ===")
                for auto in resultados:
                    print(f"ID: {auto[0]}, Modelo: {auto[1]}, Marca: {auto[2]}, Precio: {auto[3]}")
            else:
                print("La tienda no tiene autos en inventario.")

        elif opcion == "4":
            id_auto = int(input("Ingrese el ID del auto a actualizar: "))
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            actualizar_precio(id_auto, nuevo_precio)
            print("Precio actualizado correctamente.")

        elif opcion == "5":
            id_auto = int(input("Ingrese el ID del auto a eliminar: "))
            eliminar_auto(id_auto)
            print("Auto eliminado correctamente.")

        elif opcion == "6":
            print("Saliendo de la tienda. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
