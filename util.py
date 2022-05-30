from datetime import datetime


def get_date_today():
    """Metodo obtener fecha actual.

    Devuelve la fecha de HOY
    
    """
    return datetime.strptime(datetime.today().strftime('%d-%m-%Y'),'%d-%m-%Y')


def validate_date(date):
    """Metodo Valida fecha.

    Permite validar que una cadena sea una fecha valida.
    
    Parámetros:
    date -- Codena con la fecha.
    """
    try:
        a=datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def calculate_days_of_loan(book):
    """Metodo calcula dias de prestamo.

    Permite calcular los dias que han pasado desde la fecha del prestamo
    
    Parámetros:
    book -- tubla con la qury del libro
    """
    try:
        hoy= get_date_today()
        dias= hoy - datetime.strptime(book['loan_date'], '%d-%m-%Y')
        return dias.days
    except :
        return 0

def normalize_name(name):
    """Metodo normaliza nombre.

    Formatea la cadena del nombre del libro eliminando espacios y pasando a mayusculas.
    
    Parámetros:
    name -- nombre del libro
    """
    return name.strip().upper()