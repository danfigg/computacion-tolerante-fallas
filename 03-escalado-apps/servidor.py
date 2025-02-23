import socket
import threading
import json
import sys

HOST = '127.0.0.1'
PORT = 65432
servidor_activo = True 

def cargar_inventario():
    try:
        with open('inventario.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar el archivo de inventario: {e}")
        return {"inventario": []}

inventario = cargar_inventario()

def ver_inventario(cliente):
    productos = []
    for producto in inventario["inventario"]:
        productos.append({
            "id": producto['id'], 
            "nombre": producto['nombre'], 
            "categoria": producto['categoria'],
            "precio": producto['precio'], 
            "cantidad_disponible": producto['cantidad_disponible'], 
            "descripcion": producto['descripcion']
        })

    respuesta = {"accion": "ver_inventario", "inventario": productos}
    cliente.send(json.dumps(respuesta).encode('utf-8'))
    print("Inventario enviado al cliente") 

def comprar_producto(cliente, producto_id, cantidad):
    producto_encontrado = None
    for producto in inventario["inventario"]:
        if producto["id"] == producto_id:
            producto_encontrado = producto
            if producto["cantidad_disponible"] >= cantidad:
                producto["cantidad_disponible"] -= cantidad
                respuesta = {"accion": "comprar_producto", "mensaje": f"Compra realizada: {cantidad} {producto['nombre']}(s)."}
                cliente.send(json.dumps(respuesta).encode('utf-8'))
                print(f"Compra realizada: {cantidad} {producto['nombre']}(s)")
            else:
                respuesta = {"accion": "comprar_producto", "mensaje": "No hay suficiente stock."}
                cliente.send(json.dumps(respuesta).encode('utf-8'))
                print("No hay suficiente stock para la compra.")
            break
    else:
        respuesta = {"accion": "comprar_producto", "mensaje": "Producto no encontrado."}
        cliente.send(json.dumps(respuesta).encode('utf-8'))
        print("Producto no encontrado.")

def devolver_producto(cliente, producto_id, cantidad):
    producto_encontrado = None
    for producto in inventario["inventario"]:
        if producto["id"] == producto_id:
            producto_encontrado = producto
            producto["cantidad_disponible"] += cantidad
            respuesta = {"accion": "devolver_producto", "mensaje": f"Devolución realizada: {cantidad} {producto['nombre']}(s)."}
            cliente.send(json.dumps(respuesta).encode('utf-8'))
            print(f"Devolución realizada: {cantidad} {producto['nombre']}(s)")
            break
    else:
        respuesta = {"accion": "devolver_producto", "mensaje": "Producto no encontrado."}
        cliente.send(json.dumps(respuesta).encode('utf-8'))
        print("Producto no encontrado.")

def manejar_cliente(cliente, direccion):
    print(f"Cliente conectado desde {direccion}")
    while True:
        try:
            solicitud = cliente.recv(1024).decode('utf-8')
            if not solicitud:
                break

            print(f"Solicitud recibida: {solicitud}")  

            solicitud = json.loads(solicitud)
            accion = solicitud.get("accion")
            producto_id = solicitud.get("producto_id")
            cantidad = solicitud.get("cantidad")

            if accion == "ver_inventario":
                print("Acción: Ver inventario") 
                ver_inventario(cliente) 
            elif accion == "comprar_producto":
                print(f"Acción: Comprar producto ID {producto_id} cantidad {cantidad}")
                comprar_producto(cliente, producto_id, cantidad)
            elif accion == "devolver_producto":
                print(f"Acción: Devolver producto ID {producto_id} cantidad {cantidad}")
                devolver_producto(cliente, producto_id, cantidad)
            else:
                respuesta = {"accion": accion, "mensaje": "Acción no válida."}
                cliente.send(json.dumps(respuesta).encode('utf-8'))
                print("Acción no válida.")

        except Exception as e:
            print(f"Error con el cliente {direccion}: {e}")
            break

    cliente.close()
    print(f"Cliente desconectado: {direccion}")

def cerrar_servidor():
    global servidor_activo
    while True:
        comando = input("Escribe 'salir' para cerrar el servidor: ")
        if comando.lower() == "salir":
            servidor_activo = False
            print("Cerrando el servidor...")
            break

def iniciar_servidor():
    global servidor_activo
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(5)
    print("Servidor escuchando en el puerto 65432...")

    hilo_cerrar = threading.Thread(target=cerrar_servidor)
    hilo_cerrar.start()

    while servidor_activo:
        try:
            cliente, direccion = servidor.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
            hilo.start()
        except Exception as e:
            print(f"Error en el servidor: {e}")
            break

    servidor.close()
    print("Servidor cerrado.")

if __name__ == "__main__":
    iniciar_servidor()
