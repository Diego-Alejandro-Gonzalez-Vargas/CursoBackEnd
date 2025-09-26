import mysql.connector

# Conexión a la base de datos "tienda"
conexion = mysql.connector.connect(
    host="localhost",
    user="root",           # Ajusta según tu configuración
    password="PTGZU5XynS0ZhQrGWsqy",
    database="tienda"
)

cursor = conexion.cursor()

# --------- Insertar clientes ---------
clientes = [
    ("Ana Gómez", "ana@ejemplo.com"),
    ("Carlos Pérez", "carlos@ejemplo.com"),
    ("María López", "maria@ejemplo.com")
]

cursor.executemany("""
INSERT INTO clientes (nombre, correo)
VALUES (%s, %s)
""", clientes)

# --------- Insertar productos ---------
productos = [
    ("Teclado", 9000, 10),
    ("Mouse", 5000, 20),
    ("Monitor", 80000, 5)
]

cursor.executemany("""
INSERT INTO productos (nombre, precio, stock)
VALUES (%s, %s, %s)
""", productos)

# --------- Insertar ventas ---------
ventas = [
    (1, 1, 2, "2025-09-19 10:15:00"),  # Ana compra 2 Teclados
    (2, 3, 1, "2025-09-19 11:30:00")   # Carlos compra 1 Monitor
]

cursor.executemany("""
INSERT INTO ventas (cliente_id, producto_id, cantidad, fecha_venta)
VALUES (%s, %s, %s, %s)
""", ventas)

# --------- Actualizar stock ---------
# Resta stock según las ventas
actualizaciones = [
    (2, 1),  # descontar 2 del producto_id=1
    (1, 3)   # descontar 1 del producto_id=3
]

for cantidad, producto_id in actualizaciones:
    cursor.execute("""
    UPDATE productos
    SET stock = stock - %s
    WHERE id = %s
    """, (cantidad, producto_id))

# Guardar cambios
conexion.commit()
print("Datos insertados y stock actualizado correctamente.")

conexion.close()