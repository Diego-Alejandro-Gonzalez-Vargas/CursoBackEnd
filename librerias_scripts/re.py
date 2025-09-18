import re

texto = "123abc"
coincide = re.match(r'\d+', texto)   # \d+ significa "uno o más dígitos"
if coincide:
    print(coincide.group())

frase = "Hola mundo, esto es Python 3.12"
palabras = re.findall(r'\w+', frase)  # \w+ captura "palabras"
print(palabras)  # ['Hola', 'mundo', 'esto', 'es', 'Python', '3', '12']

texto = "Mi teléfono es 300-123-4567"
nuevo = re.sub(r'\d+', "X", texto)   # Reemplaza todos los dígitos por X
print(nuevo)  # Mi teléfono es XXX-XXX-XXXX