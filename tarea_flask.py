from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
uri = 'mongodb+srv://efrain12:efrainfox1212@cluster0.ak5no63.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(uri)
db = client['Prog4_III']
collection = db['tarea_m']

class Palabra:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

def exispalabra(buscar):
    palabra = collection.find_one({'palabra': buscar})
    return palabra

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        definicion = request.form['definicion']
        if exispalabra(palabra):
            return render_template('agregar.html', mensaje="La palabra ya existe.")
        else:
            collection.insert_one({'palabra': palabra, 'definicion': definicion})
            return redirect('/')
    return render_template('agregar.html')

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        palabra_obj = exispalabra(palabra)
        if palabra_obj:
            nueva_definicion = request.form['definicion']
            collection.update_one({'palabra': palabra}, {'$set': {'definicion': nueva_definicion}})
            return redirect('/')
        else:
            return render_template('editar.html', mensaje="La palabra no existe.")
    return render_template('editar.html')

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        palabra_obj = exispalabra(palabra)
        if palabra_obj:
            collection.delete_one({'palabra': palabra})
            return redirect('/')
        else:
            return render_template('eliminar.html', mensaje="La palabra no existe.")
    return render_template('eliminar.html')

@app.route('/listado')
def listado():
    palabras = collection.find({}, {'_id': 0, 'palabra': 1})
    return render_template('listado.html', palabras=palabras)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        palabra_obj = exispalabra(palabra)
        if palabra_obj:
            return render_template('buscar.html', palabra=palabra, definicion=palabra_obj['definicion'])
        else:
            return render_template('buscar.html', mensaje="La palabra no existe.")
    return render_template('buscar.html')

if __name__ == '__main__':
    app.run(debug=True)
