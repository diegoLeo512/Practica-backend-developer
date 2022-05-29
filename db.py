import sqlite3

DATABASE_NAME = "library.db"

def get_db():
    db=sqlite3.connect(DATABASE_NAME)
    return db

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS books(
                id_book INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
				creation_date TEXT NOT NULL,
                in_loan INTEGER NOT NULL,
                loan_date TEXT
            )
        """  ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
