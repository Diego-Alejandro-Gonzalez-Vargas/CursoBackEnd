# main.py
from models import Mascota, Adoptante, Refugio

def registrar_ejemplos(refugio: Refugio) -> None:
    # 3 mascotas de ejemplo
    refugio.registrar_mascota(Mascota("Luna", "Perro", 2))
    refugio.registrar_mascota(Mascota("Michi", "Gato", 1))
    refugio.registrar_mascota(Mascota("Rocky", "Perro", 4))

def mostrar_menu():
    print("\n=== Sistema de Adopción de Mascotas ===")
    print("1) Listar mascotas disponibles")
    print("2) Adoptar una mascota por nombre")
    print("3) Ver mis mascotas adoptadas")
    print("4) Salir")

def main():
    refugio = Refugio()
    registrar_ejemplos(refugio)

    # Creamos un adoptante de ejemplo
    nombre = input("Ingrese su nombre: ").strip() or "Adoptante"
    while True:
        try:
            edad_str = input("Ingrese su edad: ").strip()
            edad = int(edad_str)  # puede lanzar ValueError si no es número
            break
        except ValueError:
            print("Por favor ingrese una edad válida (número entero).")

    adoptante = Adoptante(nombre, edad)
    print(adoptante.presentarse())

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            disponibles = refugio.listar_disponibles()
            if not disponibles:
                print("No hay mascotas disponibles por ahora.")
            else:
                print("\n--- Mascotas disponibles ---")
                for m in disponibles:
                    print(f"- {m}")

        elif opcion == "2":
            nombre_mascota = input("Nombre de la mascota a adoptar: ").strip()
            exito = refugio.asignar_adopcion(nombre_mascota, adoptante)
            if exito:
                print(f"¡Felicitaciones! Ahora '{nombre_mascota}' es parte de tu familia.")

        elif opcion == "3":
            if not adoptante.mascotas_adoptadas:
                print("Aún no has adoptado mascotas.")
            else:
                print("\n--- Mis mascotas adoptadas ---")
                for m in adoptante.mascotas_adoptadas:
                    print(f"- {m}")

        elif opcion == "4":
            print("¡Gracias por usar el sistema! Hasta luego.")
            break

        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
