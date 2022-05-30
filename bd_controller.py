from db import get_db
import sqlite3

def create_book(name,date):
    """Metodo crear libro.

    Permite insertar un nuevo libro en la Base de datos
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha del libro    
    """

    #Conexion con la base de datos
    db=get_db()
    cursor = db.cursor()

    #query para insertar nuevo registro
    statement = "INSERT INTO books(name, creation_date) VALUES (?, ?)"
    try:
        cursor.execute(statement, [name, date])
        db.commit()
    except sqlite3.IntegrityError:
        return False
   
    return True

def consult_book(book_name):
    """Metodo consulta libro.

    Permite consultar el estado de un libro
    
    Parámetros:
    name -- nombre del libro
    """

    #Conexion con la base de datos
    db=get_db()
    cursor = db.cursor()

    #query para consultar el estado del libro
    statement = "SELECT * FROM books WHERE name = ?"
    cursor.execute(statement, [book_name])

    keys=('id','name','creation_date','loan_date')
    return dict(zip(keys, cursor.fetchone()))
   
def modifies_book(book_name,date):
    """Metodo Modifica libro.

    Permite modificar la fecha de prestamo de un libro
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha nueva
    """

    #Conexion DB
    db=get_db()
    cursor = db.cursor()


    #query para modificar la fecha de prestamo del libro @name
    statement = "UPDATE books SET loan_date = ? WHERE name = ?"
    cursor.execute(statement, [date,book_name])
    db.commit()


    
def delete_book(book_name):
    """Metodo Elimina libro.

    Permite Eliminar un libro  de la base de datos
    
    Parámetros:
    name -- nombre del libro
    """
    #Conexion DB
    db=get_db()
    cursor = db.cursor()

    #query para Eliminar el libro @name
    statement = "DELETE FROM books WHERE name = ?;"
    cursor.execute(statement, [book_name])
    db.commit()
   
def consult_book_list():
    """Metodo consulta lista de libros.

    Permite obtener una lista de todos los librso almacenados.

    """

    #Conexion DB
    db=get_db()
    cursor = db.cursor()

    #query para consultar la lista
    statement = "SELECT id_book, name FROM books"
    keys=('id','name')
    cursor.execute(statement, [])
    return cursor.fetchall()
    return dict(zip(keys, cursor.fetchone()))