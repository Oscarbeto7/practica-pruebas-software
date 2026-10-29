def validar_numeros(*args):
    for n in args:
        if not isinstance(n, (int, float)):
            raise TypeError("Los argumentos deben ser numéricos")

def sumar(a, b):
    validar_numeros(a, b)
    return a + b

def restar(a, b):
    validar_numeros(a, b)
    return a - b

def multiplicar(a, b):
    validar_numeros(a, b)
    return a * b

def dividir(a, b):
    validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b