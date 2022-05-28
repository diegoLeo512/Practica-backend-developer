from bd_controller import insert_new_book
from db import create_tables

if __name__ == "__main__":
    create_tables()
    insert_new_book('prueba 1','11-02-45')
