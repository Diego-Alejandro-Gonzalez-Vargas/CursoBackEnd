
def saludar(nombre):
    return f"Hola, {nombre}!"

print("Esto siempre se ejecuta al cargar el módulo")
print("El valor de __name__ en mimodulo.py es:", __name__)

if __name__ == "__main__":
    print("Este código se ejecuta SOLO si corres mimodulo.py directamente")
    print(saludar("Estudiante"))