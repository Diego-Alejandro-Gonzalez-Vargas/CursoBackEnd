import mi_paquete.operaciones as idunico

# print("Versión del paquete:", mi_paquete.VERSION)
print("Suma:", idunico.sumar(3, 4))
# print("Saludo:", mi_paquete.saludar("Diego"))

# También se puede importar módulos internos
from mi_paquete import operaciones
print("Resta:", operaciones.restar(10, 5))