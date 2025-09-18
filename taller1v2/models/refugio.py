# models/refugio.py
from .helpers import buscar_mascota

class Refugio:
    def __init__(self):
        # atributo "privado" por convención con name mangling
        self.__mascotas = []  # lista de Mascota

    def registrar_mascota(self, mascota) -> None:
        self.__mascotas.append(mascota)

    def listar_disponibles(self) -> list:
        return [m for m in self.__mascotas if not m.adoptado]

    def asignar_adopcion(self, nombre_mascota: str, adoptante) -> bool:
        """
        Busca la mascota y asigna adopción si está disponible.
        Maneja errores mostrando mensajes desde esta clase (según el taller).
        """
        try:
            mascota = buscar_mascota(nombre_mascota, self.__mascotas)
            if mascota is None:
                # raise con ValueError (tema de manejo de errores)
                raise ValueError(f"No existe una mascota registrada con el nombre '{nombre_mascota}'.")

            if mascota.adoptado:
                raise ValueError(f"La mascota '{mascota.nombre}' ya fue adoptada.")

            # Caso feliz
            mascota.adoptado = True
            adoptante.adoptar(mascota)
            return True

        except ValueError as e:
            # Mensaje "desde la clase", sin detener el programa
            print(f"[Refugio] {e}")
            return False
