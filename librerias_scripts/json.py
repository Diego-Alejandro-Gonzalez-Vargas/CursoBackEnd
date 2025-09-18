import json

datos = {"nombre": "Ana", "edad": 25}
json_str = json.dumps(datos)   # Convierte a cadena JSON
print(json_str)  
json_str = '{"nombre": "Carlos", "edad": 30}'
persona = json.loads(json_str)  # Convierte a diccionario de Python
print(persona["nombre"]) 

with open("persona.json", "w") as f:
    json.dump(datos, f)

with open("C:/Users/Diego/misCosas/clases/codigo/clase5/persona.json", "r") as f:
    persona = json.load(f)
print(persona)