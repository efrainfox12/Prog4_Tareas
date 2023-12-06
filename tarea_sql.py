from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:efrainfox1212@localhost/diccionario_panamenian")
class Diccionario(Base):
    __tablename__ = "diccionario"
    palabra = Column(String(length=15), primary_key=True)
    definicion = Column(String(length=25))  # Cambiado de "significado" a "definicion"

    def __init__(self, palabra, definicion):  # Cambiado de "significado" a "definicion"
        self.palabra = palabra
        self.definicion = definicion  # Cambiado de "significado" a "definicion"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def exispalabra(buscar, Diccionario):
    buscar = session.query(Diccionario).filter_by(palabra=buscar).first()
    return buscar

def aggpalabra(Diccionario):
    print("\n¡Vamos agregar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribir nueva palabra: ")
        buscar = exispalabra(palabra, Diccionario)
        if buscar:
            print("\nLa palabra ya existe")
        else:
            definicion = input("\nEscribir definición: ")  # Cambiado de "significado" a "definicion"
            registro = Diccionario(palabra=palabra, definicion=definicion)  # Cambiado de "significado" a "definicion"
            session.add(registro)
            session.commit()
            print("\n¡Palabra agregada con éxito!")
            continuar = False

def editpalabra(Diccionario):
    print("\n¡Vamos a editar una palabra!")
    continuar = True
    while continuar:
        palabra = input("\nEscribe la palabra a editar: ").lower()
        buscar = exispalabra(palabra, Diccionario)
        if not buscar:
            print("\nLa palabra no existe")
        else:
            nueva_palabra = input("\nEscribe el nuevo significado: ")
            palabraedit = session.query(Diccionario).filter_by(palabra=palabra).first()
            palabraedit.significado = nueva_palabra
            session.commit()
            print("\nPalabra editada con éxito")
            continuar = False


def delpalabra(Diccionario):
    print("\n¡Eliminar una palabra!")
    palabra = input("\nEscribe la palabra a eliminar: ").lower()
    buscar = exispalabra(palabra, Diccionario)
    if not buscar:
        print("\nLa palabra no existe")
    else:
        confirmacion = input(f"\n¿Estás seguro de que deseas eliminar la palabra '{palabra}'? (Sí/No): ").lower()
        if confirmacion == "si" or confirmacion == "s":
            session.delete(buscar)
            session.commit()
            print("\nPalabra eliminada con éxito")
        else:
            print("\nOperación de eliminación cancelada")


def listpalabra(Diccionario):
    print("\n¡Listado de palabras!")
    palabras = session.query(Diccionario.palabra).all()
    if not palabras:
        print("Diccionario vacío, intenta añadir una palabra primero")
    else:
        for palabra in palabras:
            print(palabra[0])


def signpalabra(Diccionario):
    print("\n¡Vamos a buscar un significado!")
    continuar = True
    while continuar:
        palabra = input("\nEscriba la palabra para buscar su significado: ")
        buscar = palabra.lower()
        registro = session.query(Diccionario).filter_by(palabra=buscar).first()
        if registro:
            print(f"\n{palabra}: {registro.definicion}")
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
            aggpalabra(Diccionario)
        elif opcion == 2:
            editpalabra(Diccionario)
        elif opcion == 3:
            delpalabra(Diccionario)
        elif opcion == 4:
            listpalabra(Diccionario)
        elif opcion == 5:
            signpalabra(Diccionario)
        elif opcion == 6:
            print("¡Hasta luego!")
            session.close()
            exit()

if __name__ == "__main__":
        menu()