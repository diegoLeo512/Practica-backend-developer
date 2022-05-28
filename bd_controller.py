from db import get_db
import sqlite3

def insert_new_book(name,date):
    db=get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(name, creation_date) VALUES (?, ?)"
    try:
        cursor.execute(statement, [name, date])
        db.commit()
    except sqlite3.IntegrityError:
        return False
   
    return True

