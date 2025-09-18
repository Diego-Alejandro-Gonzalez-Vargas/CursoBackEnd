# models/mascota.py

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, adoptado: bool = False):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = adoptado

    def __str__(self) -> str:
        estado = "Adoptado" if self.adoptado else "Disponible"
        return f"Mascota(nombre='{self.nombre}', especie='{self.especie}', edad={self.edad}, estado={estado})"
