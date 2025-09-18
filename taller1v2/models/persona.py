
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self) -> str:
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


class Adoptante(Persona):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)  # herencia + super()
        self.mascotas_adoptadas = []    # lista vacía por defecto

    def adoptar(self, mascota) -> None:
        """Agrega la mascota a la lista del adoptante."""
        self.mascotas_adoptadas.append(mascota)
