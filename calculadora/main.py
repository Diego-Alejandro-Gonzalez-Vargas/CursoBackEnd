
import calculadora
# calculadora.py
"""
Módulo que proporciona funciones matemáticas básicas.
"""
print(calculadora.sumar(5, 3))  # 8
print(calculadora.restar(10, 4))  # 6
print(calculadora.PI)  # 3.14159
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b
# # También podemos importar elementos específicos
# from calculadora import sumar, PI
# print(sumar(7, 2))  # 9
# print(PI)  # 3.14159
