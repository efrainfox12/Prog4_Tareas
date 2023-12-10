from pymongo import MongoClient


uri = 'mongodb+srv://efrain12:efrainfox1212@cluster0.ak5no63.mongodb.net/?retryWrites=true&w=majority'
db = MongoClient(uri)['Prog4_III']
collection = db['tarea_m']

class Diccionario:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

def exispalabra(buscar):
    return collection.find_one({'palabra': buscar})

def aggpalabra():
    print("\n¡Vamos agregar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribir nueva palabra: ")
        buscar = exispalabra(palabra)
        if buscar:
            print("\nLa palabra ya existe")
        else:
            definicion = input("\nEscribir definición: ")
            registro = {'palabra': palabra, 'definicion': definicion}
            collection.insert_one(registro)
            print("\n¡Palabra agregada con éxito!")
            continuar = False

def editpalabra():
    print("\n¡Vamos a editar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribe la palabra a editar: ").lower()
        buscar = exispalabra(palabra)
        if not buscar:
            print("\nLa palabra no existe")
        else:
            nueva_definicion = input("\nEscribe el nuevo significado: ")
            collection.update_one({'palabra': palabra}, {'$set': {'definicion': nueva_definicion}})
            print("\nPalabra editada con éxito")
            continuar = False

def delpalabra():
    print("\n¡Eliminar una palabra!")
    palabra = input("\nEscribe la palabra a eliminar: ").lower()
    buscar = exispalabra(palabra)
    if not buscar:
        print("\nLa palabra no existe")
    else:
        confirmacion = input(f"\n¿Estás seguro de que deseas eliminar la palabra '{palabra}'? (Sí/No): ").lower()
        if confirmacion == "si" or confirmacion == "s":
            collection.delete_one({'palabra': palabra})
            print("\nPalabra eliminada con éxito")
        else:
            print("\nOperación de eliminación cancelada")

def listpalabra():
    print("\n¡Listado de palabras!")
    palabras = collection.find({}, {'_id': 0, 'palabra': 1})
    palabras = [palabra['palabra'] for palabra in palabras]
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
        buscar = exispalabra(palabra)
        if buscar:
            print(f"\n{palabra}: {buscar['definicion']}")
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
