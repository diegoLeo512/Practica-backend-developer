import sqlite3

DATABASE_NAME = "library.db"

def get_db():
    """Metodo Obtener base de datos.

    Conecta con al base de datos
    
    """

    db=sqlite3.connect(DATABASE_NAME)
    return db

def create_tables():
    """Metodo Crea tablas.

    Crea la tabla de base de datos si no existe ya.
    
    Parámetros:
    name -- nombre del libro
    """
    
    tables = [
        """CREATE TABLE IF NOT EXISTS books(
                id_book INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
				creation_date TEXT NOT NULL,
                loan_date TEXT
            )
        """  ]

    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
