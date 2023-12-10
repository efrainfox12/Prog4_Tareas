import redis

# Establecer conexión a Redis
redis_client = redis.StrictRedis(host='redis-17709.c279.us-central1-1.gce.redns.redis-cloud.com', port=17709
, db=0, password= '7eTSlWYJLF0y9truR9Dnf3nI6YxgHSqF')

class Diccionario:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

def exispalabra(buscar):
    definicion = redis_client.hget('diccionario', buscar)
    return definicion

def aggpalabra():
    print("\n¡Vamos agregar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribir nueva palabra: ")
        definicion = exispalabra(palabra)
        if definicion:
            print("\nLa palabra ya existe")
        else:
            nueva_definicion = input("\nEscribir definición: ")
            redis_client.hset('diccionario', palabra, nueva_definicion)
            print("\n¡Palabra agregada con éxito!")
            continuar = False

def editpalabra():
    print("\n¡Vamos a editar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribe la palabra a editar: ").lower()
        definicion = exispalabra(palabra)
        if not definicion:
            print("\nLa palabra no existe")
        else:
            nueva_definicion = input("\nEscribe el nuevo significado: ")
            redis_client.hset('diccionario', palabra, nueva_definicion)
            print("\nPalabra editada con éxito")
            continuar = False

def delpalabra():
    print("\n¡Eliminar una palabra!")
    palabra = input("\nEscribe la palabra a eliminar: ").lower()
    definicion = exispalabra(palabra)
    if not definicion:
        print("\nLa palabra no existe")
    else:
        confirmacion = input(f"\n¿Estás seguro de que deseas eliminar la palabra '{palabra}'? (Sí/No): ").lower()
        if confirmacion == "si" or confirmacion == "s":
            redis_client.hdel('diccionario', palabra)
            print("\nPalabra eliminada con éxito")
        else:
            print("\nOperación de eliminación cancelada")

def listpalabra():
    print("\n¡Listado de palabras!")
    palabras = redis_client.hkeys('diccionario')
    if not palabras:
        print("Diccionario vacío, intenta añadir una palabra primero")
    else:
        for palabra in palabras:
            print(palabra)

def signpalabra():
    print("\n¡Vamos a buscar un significado!")
    continuar = True
    while continuar:
        palabra = input("\nEscriba la palabra para buscar su significado: ")
        definicion = exispalabra(palabra)
        if definicion:
            print(f"\n{palabra}: {definicion}")
            continuar = False
        else:
            print(f"\nNo se encontró el significado de {palabra}.")

def menu():
    while True:
        print("\n\n--<| DICCIONARIO PANAMEÑO |>--")
        print("1. Agregar nueva palabra.")
        print("2. Editar palabra existente.")
        print("3. Eliminar palabra existente.")
        print("4. Ver listado de palabras.")
        print("5. Buscar significado de palabra.")
        print("6. Salir.")
        try:
            opcion = int(input("Opcion: "))
        except:
            print("ERR::Opcion invalida.")
            opcion = 999

        if opcion == 1:
            aggpalabra()
        elif opcion == 2:
            editpalabra()
        elif opcion == 3:
            delpalabra()
        elif opcion == 4:
            listpalabra()
        elif opcion == 5:
            signpalabra()
        elif opcion == 6:
            print("¡Hasta luego!")
            exit()

if __name__ == "__main__":
    menu()
