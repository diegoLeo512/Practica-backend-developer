from db import get_db
import sqlite3

def create_book(name,date):
    db=get_db()
    cursor = db.cursor()
    statement = "INSERT INTO books(name, creation_date,in_loan) VALUES (?, ?, ?)"
    try:
        cursor.execute(statement, [name, date, 0])
        db.commit()
    except sqlite3.IntegrityError:
        return False
   
    return True

def consult_book(book_name):
    db=get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM books WHERE name = ?"
    result=cursor.execute(statement, [book_name])
    return cursor.fetchone()
   
def modifies_book(book_name,date):
    db=get_db()
    cursor = db.cursor()
    statement = "UPDATE books SET loan_date = ? WHERE name = ?"
    result=cursor.execute(statement, [date,book_name])
    print(cursor.fetchone())
    return cursor.fetchone()
    
def delete_book(book_name):
    db=get_db()
    cursor = db.cursor()
    statement = "DELETE FROM books WHERE name = ?;"
    result=cursor.execute(statement, [book_name])
    return cursor.fetchone()
