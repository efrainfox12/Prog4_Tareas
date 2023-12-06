import sqlite3


def crear_tabla():
    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diccionario (
            palabra TEXT PRIMARY KEY,
            significado TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()


def agregar_palabra():
    palabra = input("Ingresa una palabra: ")
    significado = input(f"Ingresa el significado de '{palabra}': ")

    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute("INSERT OR REPLACE INTO diccionario (palabra, significado) VALUES (?, ?)", (palabra, significado))

    conexion.commit()
    conexion.close()
    print(f"La palabra '{palabra}' ha sido agregada al diccionario.")


def editar_palabra():
    palabra = input("Ingresa la palabra que deseas editar: ")
    nuevo_significado = input(f"Ingresa el nuevo significado de '{palabra}': ")

    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute("UPDATE diccionario SET significado=? WHERE palabra=?", (nuevo_significado, palabra))

    conexion.commit()
    conexion.close()
    print(f"El significado de '{palabra}' ha sido actualizado.")


def eliminar_palabra():
    palabra = input("Ingresa la palabra que deseas eliminar: ")

    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM diccionario WHERE palabra=?", (palabra,))

    conexion.commit()
    conexion.close()
    print(f"La palabra '{palabra}' ha sido eliminada del diccionario.")


def ver_listado():
    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT palabra FROM diccionario")
    palabras = cursor.fetchall()

    conexion.close()

    if palabras:
        print("\nListado de palabras:")
        for palabra in palabras:
            print(palabra[0])
    else:
        print("\nEl diccionario está vacío.")


def buscar_significado():
    palabra = input("Ingresa la palabra para buscar su significado: ")

    conexion = sqlite3.connect('diccionario_prog4.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT significado FROM diccionario WHERE palabra=?", (palabra,))
    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        print(f"\nSignificado de '{palabra}': {resultado[0]}")
    else:
        print("\nPalabra no encontrada.")


# Crear la tabla si no existe
crear_tabla()

while True:
    print("\n--- Menú ---")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra existente")
    print("e) Ver listado de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")

    opcion = input("Selecciona una opción (a, c, d, e, f, g): ")

    if opcion == "a":
        agregar_palabra()
    elif opcion == "c":
        editar_palabra()
    elif opcion == "d":
        eliminar_palabra()
    elif opcion == "e":
        ver_listado()
    elif opcion == "f":
        buscar_significado()
    elif opcion == "g":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Ingresa una letra válida (a, c, d, e, f, g).")
