from db import get_db
import sqlite3

def insert_new_book(name,date):
    db=get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(name, creation_date,in_loan) VALUES (?, ?, ?)"
    try:
        cursor.execute(statement, [name, date, 0])
        db.commit()
    except sqlite3.IntegrityError:
        return False
   
    return True

def get_book(id):
    db=get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM books WHERE id_book = ?"
    cursor.execute(statement, [id])
    print(cursor.fetchone())
