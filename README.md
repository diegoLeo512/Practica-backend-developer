# Practica-backend-developer
Instrucciones basicas:
Para ejecutar servicio web, ejecutar el archivo main.py.
Para ejecutar los test, ejecutar el archivo tests.py.


Descripcion de las tecnologias usadas:
El servicio web REST se implemento en Python 3 usando el framework Flask 2.1.2 (https://flask.palletsprojects.com/en/2.1.x/). 
Para el testeo de la aplicacion, se realizaron pruebas funcionales con Postman ( https://www.postman.com/ ) y se construyeron pruebas unitarias para los metodos CRUD usando el framework Unittest (https://docs.python.org/3/library/unittest.html) de Python.
El modelo de datos se construyo sobre SQL, concretamente con SQLite3 (https://www.sqlite.org/index.html).


Descripcion de metodos :

ruta: /books metodo GET #################################################################

Operacion CRUD GET para el recurso libro.

    devuelve las propiedades de un libro y dias transcurrido desde el prestamo
    

    Parámetros:
    name -- nombre del libro    

########################################################################################

ruta: /books metodo POST ###############################################################

    Operacion CRUD POST para el recurso libro.

    Crea un nuevo libro
    

    Parámetros:
    name -- nombre del libro
    date -- Fecha del libro    

########################################################################################

ruta: /books' metodo PUT ###############################################################

    Operacion CRUD PUT para el recurso libro.

    Permite introducir/cambiar la fecha de prestamo de un libro
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha de prestamo del libro    
    
########################################################################################

ruta: /books metodo DELETE #############################################################
    
    Operacion CRUD DELETE para el recurso libro.

    Elimina un libro de la base de datos
    
    Parámetros:
    name -- nombre del libro
    date -- Fecha de prestamo del libro    

########################################################################################

ruta: /books/list metodo GET ###########################################################
    
    Operacion CRUD GET para el recurso libro.

    obtiene una lista de los libros almacenados
    
########################################################################################


