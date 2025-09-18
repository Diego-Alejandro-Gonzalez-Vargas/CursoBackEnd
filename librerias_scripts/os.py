import os
print(os.getcwd())

os.mkdir("nueva_carpeta")      # Crear carpeta

os.rmdir("nueva_carpeta")      # Eliminar carpeta vacía

archivos = os.listdir(".")   # Lista archivos en el directorio actual
print(archivos)

ruta = os.path.join("carpeta", "archivo.txt")
print(ruta)  # carpeta/archivo.txt (ajustado al sistema)