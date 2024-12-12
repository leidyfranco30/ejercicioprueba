import pytest
from operaciones import Operaciones, suma, resta, multiplicar, dividir

def test_suma():
    assert suma(4, 4) == 8
    assert suma(-4, -4) == -8

def test_resta():
    assert resta(4, 4) == 0
    assert resta(-4, -4) == 0

def test_multiplicar():
    assert multiplicar(4, 4) == 16
    assert multiplicar(-4, -4) == 16

def test_dividir():
    assert dividir(4, 4) == 1
    assert dividir(-8, -4) == 2
    assert dividir(4, 0) == "La división por cero no es válida, se indetermina"
