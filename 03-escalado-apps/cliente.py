import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def enviar_solicitud(cliente, accion, producto_id=None, cantidad=None):
    try:
        solicitud = {"accion": accion}
        if producto_id:
            solicitud["producto_id"] = producto_id
        if cantidad:
            solicitud["cantidad"] = cantidad
        
        cliente.send(json.dumps(solicitud).encode('utf-8'))
        respuesta = cliente.recv(1024).decode('utf-8')
        respuesta = json.loads(respuesta)
        
        if "inventario" in respuesta:
            print("\nInventario disponible:")
            for producto in respuesta["inventario"]:
                print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']} USD, Stock: {producto['cantidad_disponible']}")
        else:
            print(respuesta["mensaje"])
    except json.JSONDecodeError:
        print("Error al procesar la respuesta del servidor.")
    except socket.error as e:
        print(f"Error de comunicación con el servidor: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_menu(cliente):
    while True:
        print("\nMenú de la Tienda Nike")
        print("1. Ver inventario")
        print("2. Comprar producto")
        print("3. Devolver producto")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            enviar_solicitud(cliente, "ver_inventario")
        elif opcion == "2":
            producto_id = input("Introduce el ID del producto que deseas comprar: ")
            cantidad = int(input("Introduce la cantidad que deseas comprar: "))
            enviar_solicitud(cliente, "comprar_producto", producto_id, cantidad)
        elif opcion == "3":
            producto_id = input("Introduce el ID del producto que deseas devolver: ")
            cantidad = int(input("Introduce la cantidad que deseas devolver: "))
            enviar_solicitud(cliente, "devolver_producto", producto_id, cantidad)
        elif opcion == "4":
            print("Saliendo de la tienda...")
            cliente.close()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    mostrar_menu(cliente)

if __name__ == "__main__":
    iniciar_cliente()
