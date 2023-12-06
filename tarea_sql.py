import mysql.connector

def conectar():
    # Función para conectarse a la base de datos
    DB_URL = "mysql+mysqlconnector://root:efrainfox1212@localhost:3306/diccionario_panamenian"
    return DB_URL

def crear_tablas():
    # Función para crear las tablas necesarias
    conexion = conectar()
    cursor = conexion.cursor()

    # Crear la tabla de palabras
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabra (
            id INT AUTO_INCREMENT PRIMARY KEY,
            palabra VARCHAR(255) NOT NULL
        )
    """)

    # Crear la tabla de significados
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS significado (
            id INT AUTO_INCREMENT PRIMARY KEY,
            significado TEXT NOT NULL
        )
    """)

    # Crear la tabla de relación entre palabra y significado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS palabra_significado (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_palabra INT,
            id_significado INT,
            FOREIGN KEY (id_palabra) REFERENCES palabra(id),
            FOREIGN KEY (id_significado) REFERENCES significado(id)
        )
    """)

    conexion.commit()
    conexion.close()

def consultar_diccionario():
    # Función para consultar todas las palabras y significados en el diccionario
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT palabra.palabra, significado.significado
        FROM palabra
        JOIN palabra_significado ON palabra.id = palabra_significado.id_palabra
        JOIN significado ON palabra_significado.id_significado = significado.id
    """)

    resultados = cursor.fetchall()

    for resultado in resultados:
        print(f"{resultado[0]}: {resultado[1]}")

    conexion.close()

def agregar_palabra_y_significado(palabra, significado):
    # Función para agregar una nueva palabra y su significado al diccionario
    conexion = conectar()
    cursor = conexion.cursor()

    # Insertar la palabra en la tabla 'palabra'
    cursor.execute("INSERT INTO palabra (palabra) VALUES (%s)", (palabra,))
    id_palabra = cursor.lastrowid

    # Insertar el significado en la tabla 'significado'
    cursor.execute("INSERT INTO significado (significado) VALUES (%s)", (significado,))
    id_significado = cursor.lastrowid

    # Crear la relación en la tabla 'palabra_significado'
    cursor.execute("INSERT INTO palabra_significado (id_palabra, id_significado) VALUES (%s, %s)", (id_palabra, id_significado))

    conexion.commit()
    conexion.close()

# Crear las tablas necesarias
crear_tablas()

# Ejemplos de uso
# Consultar todas las palabras en el diccionario
consultar_diccionario()

# Agregar una nueva palabra y su significado
agregar_palabra_y_significado("Python", "Lenguaje de programación de alto nivel")

# Consultar el diccionario después de agregar una nueva palabra y su significado
consultar_diccionario()
