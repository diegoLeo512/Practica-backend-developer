from flask import Flask, jsonify, request
import bd_controller
from db import create_tables
from util import *

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_book():
    """Operacion CRUD GET para el recurso libro.

    devuelve las propiedades de un libro y dias transcurrido desde el prestamo
    

    Parámetros:
    name -- nombre del libro    
    """

    #parametro name
    name = request.args.get('name')

    #Validacion parametro
    if name is None:
        return jsonify("parametro name faltante")

    #normalizar nombre
    name=normalize_name(name)
    
    #conexion DB
    book = bd_controller.consult_book(name)
    #Calculo de dias
    days=calculate_days_of_loan(book)
    book['loan_days']=days

    return jsonify(book)

@app.route('/books', methods=["POST"])
def post_book():
    """Operacion CRUD POST para el recurso libro.

    Crea un nuevo libro
    

    Parámetros:
    name -- nombre del libro
    date -- Fecha del libro    
    """
    #parametro name
    name = request.args.get('name')
    if name is None:
        return jsonify("parametro name faltante")
    name=normalize_name(name)

    #parametro date
    date = request.args.get('date')
    if date is None:
        return jsonify("parametro date faltante")

    #Validacion de fecha valida
    if not validate_date(date):
        return jsonify("parametro date invalido")

    #conexion DB
    result = bd_controller.create_book(name,date)
    
    if result:
        msg="Libro creado correctamente"
    else:
        msg="Error, el libro ya existe"

    return jsonify(msg)



@app.route('/books', methods=["PUT"])
def put_book():
    """Operacion CRUD PUT para el recurso libro.

    Permite introducir/cambiar la fecha de prestamo de un libro
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha de prestamo del libro    
    """

    #Parametro name
    name = request.args.get('name')
    if name is None:
        return jsonify("parametro name faltante")
    name=normalize_name(name)

    #Parametro date
    date = request.args.get('date')
    if date is None :
        return jsonify("parametro date faltante")

    #Validacion de valor valido de fecha 
    if date == 'NULL' or validate_date(date):
        #Conexion DB
        bd_controller.modifies_book(name,date)
        return jsonify('Ok')
    else :
        return jsonify('Fecha invalida')

@app.route('/books', methods=["DELETE"])
def delete_book():
    """Operacion CRUD DELETE para el recurso libro.

    Elimina un libro de la base de datos
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha de prestamo del libro    
    """

    #Parametro name
    name = request.args.get('name')
    if name is None:
        return jsonify("parametro name faltante")
    name=normalize_name(name)

    #Conexion DB
    bd_controller.delete_book(name)
    return jsonify('ok')


@app.route('/books/list', methods=["GET"])
def get_book_list():
    """Operacion CRUD GET para el recurso libro.

    obtiene una lista de los libros almacenados
    
    """
        
    list = bd_controller.consult_book_list()
  
    return jsonify(list)