def buscar_mascota(nombre: str, lista_mascotas: list):
    """Devuelve la mascota cuyo nombre coincida exactamente, o None si no existe."""
    for m in lista_mascotas:
        if m.nombre.lower() == nombre.lower():
            return m
    return None