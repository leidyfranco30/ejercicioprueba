from enum import Enum 

class Operaciones(Enum):
    SUMA = "suma"
    RESTA = "resta"
    MULTIPLICAR = "multiplicar"
    DIVIDIR = "dividir"

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "La división por cero no es válida, se indetermina"

