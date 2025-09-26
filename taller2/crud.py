# crud.py
from database import get_connection

def listar_clientes():
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        cur.execute("SELECT id, nombre, correo FROM clientes ORDER BY id")
        filas = cur.fetchall()
        return filas
    except Exception as e:
        print("Error al listar clientes:", e)
        return []
    finally:
        if conexion is not None:
            conexion.close()

def listar_productos():
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        cur.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY id")
        filas = cur.fetchall()
        return filas
    except Exception as e:
        print("Error al listar productos:", e)
        return []
    finally:
        if conexion is not None:
            conexion.close()

def listar_ventas():
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        sql = """
        SELECT v.id, c.nombre AS cliente, p.nombre AS producto, v.cantidad, v.fecha_venta
        FROM ventas v
        INNER JOIN clientes c ON v.cliente_id = c.id
        INNER JOIN productos p ON v.producto_id = p.id
        ORDER BY v.id
        """
        cur.execute(sql)
        filas = cur.fetchall()
        return filas
    except Exception as e:
        print("Error al listar ventas:", e)
        return []
    finally:
        if conexion is not None:
            conexion.close()

def agregar_cliente(nombre, correo):
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        cur.execute("INSERT INTO clientes (nombre, correo) VALUES (%s, %s)", (nombre, correo))
        conexion.commit()
        print("Cliente agregado. ID:", cur.lastrowid)
    except Exception as e:
        if conexion is not None:
            conexion.rollback()
        print("Error al agregar cliente:", e)
    finally:
        if conexion is not None:
            conexion.close()

def agregar_producto(nombre, precio, stock):
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        cur.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
                    (nombre, precio, stock))
        conexion.commit()
        print("Producto agregado. ID:", cur.lastrowid)
    except Exception as e:
        if conexion is not None:
            conexion.rollback()
        print("Error al agregar producto:", e)
    finally:
        if conexion is not None:
            conexion.close()

def registrar_venta(cliente_id, producto_id, cantidad):
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()

        # Transacción explícita
        cur.execute("START TRANSACTION")

        # Verificar stock y bloquear fila del producto
        cur.execute("SELECT stock FROM productos WHERE id = %s FOR UPDATE", (producto_id,))
        fila = cur.fetchone()
        if fila is None:
            raise Exception("Producto inexistente.")
        stock_actual = fila[0]

        if cantidad <= 0:
            raise Exception("Cantidad debe ser positiva.")
        if stock_actual < cantidad:
            raise Exception("Stock insuficiente. Actual: " + str(stock_actual))

        # Insertar venta (fecha automática)
        cur.execute(
            "INSERT INTO ventas (cliente_id, producto_id, cantidad) VALUES (%s, %s, %s)",
            (cliente_id, producto_id, cantidad)
        )

        # Actualizar stock
        nuevo_stock = stock_actual - cantidad
        cur.execute("UPDATE productos SET stock = %s WHERE id = %s", (nuevo_stock, producto_id))

        conexion.commit()
        print("Venta registrada. Nuevo stock:", nuevo_stock)
    except Exception as e:
        if conexion is not None:
            conexion.rollback()
        print("Error al registrar venta:", e)
    finally:
        if conexion is not None:
            conexion.close()

def actualizar_producto(producto_id, nuevo_nombre, nuevo_precio, nuevo_stock):
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()
        cur.execute(
            "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s",
            (nuevo_nombre, nuevo_precio, nuevo_stock, producto_id)
        )
        conexion.commit()
        print("Producto actualizado. Filas modificadas:", cur.rowcount)
    except Exception as e:
        if conexion is not None:
            conexion.rollback()
        print("Error al actualizar producto:", e)
    finally:
        if conexion is not None:
            conexion.close()

def eliminar_venta(venta_id):
    conexion = None
    try:
        conexion = get_connection()
        cur = conexion.cursor()

        # Ver la venta antes de borrarla
        cur.execute("""
        SELECT v.id, c.nombre, p.nombre, v.cantidad, v.fecha_venta
        FROM ventas v
        INNER JOIN clientes c ON v.cliente_id = c.id
        INNER JOIN productos p ON v.producto_id = p.id
        WHERE v.id = %s
        """, (venta_id,))
        venta = cur.fetchone()
        if venta is None:
            print("No existe la venta:", venta_id)
            return

        cur.execute("DELETE FROM ventas WHERE id = %s", (venta_id,))
        conexion.commit()
        print("Venta eliminada:", venta)
    except Exception as e:
        if conexion is not None:
            conexion.rollback()
        print("Error al eliminar venta:", e)
    finally:
        if conexion is not None:
            conexion.close()
