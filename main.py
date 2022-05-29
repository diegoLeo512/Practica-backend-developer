from asyncio.windows_events import NULL
from bd_controller import consult_book, modifies_book, delete_book, create_book
from db import create_tables

if __name__ == "__main__":
    create_tables()
    #create_book('prueba 3','11-02-45')
    #get_book('prueba 3')
    modifies_book(None,NULL)


