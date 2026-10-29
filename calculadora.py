def sumar(a, b):
    return a + b

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser numéricos")
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b