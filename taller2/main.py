# main.py
from crud import (
    listar_clientes, listar_productos, listar_ventas,
    agregar_cliente, agregar_producto,
    registrar_venta, actualizar_producto, eliminar_venta
)

def pedir_entero(msg):
    valor = input(msg)
    while not valor.isdigit():
        print("Debe ser un número entero.")
        valor = input(msg)
    return int(valor)

def menu():
    print("\n===== MENÚ TIENDA =====")
    print("1. Listar clientes")
    print("2. Listar productos")
    print("3. Listar ventas")
    print("4. Agregar cliente")
    print("5. Agregar producto")
    print("6. Registrar venta")
    print("7. Actualizar producto")
    print("8. Eliminar venta (verificar cuál)")
    print("0. Salir")

def main():
    opcion = -1
    while opcion != 0:
        menu()
        try:
            opcion = int(input("Opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            opcion = -1
            continue

        if opcion == 1:
            filas = listar_clientes()
            print("\n-- CLIENTES --")
            for f in filas:
                print("ID:", f[0], "| Nombre:", f[1], "| Correo:", f[2])

        elif opcion == 2:
            filas = listar_productos()
            print("\n-- PRODUCTOS --")
            for f in filas:
                print("ID:", f[0], "| Nombre:", f[1], "| Precio:", f[2], "| Stock:", f[3])

        elif opcion == 3:
            filas = listar_ventas()
            print("\n-- VENTAS --")
            for f in filas:
                print("ID:", f[0], "| Cliente:", f[1], "| Producto:", f[2],
                      "| Cantidad:", f[3], "| Fecha:", f[4])

        elif opcion == 4:
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            agregar_cliente(nombre, correo)

        elif opcion == 5:
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
            except ValueError:
                print("Precio inválido.")
                continue
            stock = pedir_entero("Stock: ")
            agregar_producto(nombre, precio, stock)

        elif opcion == 6:
            cliente_id = pedir_entero("ID Cliente: ")
            producto_id = pedir_entero("ID Producto: ")
            cantidad = pedir_entero("Cantidad: ")
            registrar_venta(cliente_id, producto_id, cantidad)

        elif opcion == 7:
            producto_id = pedir_entero("ID Producto a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            try:
                nuevo_precio = float(input("Nuevo precio: "))
            except ValueError:
                print("Precio inválido.")
                continue
            nuevo_stock = pedir_entero("Nuevo stock: ")
            actualizar_producto(producto_id, nuevo_nombre, nuevo_precio, nuevo_stock)

        elif opcion == 8:
            venta_id = pedir_entero("ID de venta a eliminar: ")
            eliminar_venta(venta_id)

        elif opcion == 0:
            print("Saliendo...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
