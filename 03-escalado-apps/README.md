# Sistema de Inventario con Servidor Cliente

Este proyecto es un sistema de gestión de inventario que utiliza un servidor y cliente para interactuar con los productos almacenados. El servidor maneja las solicitudes de los clientes y permite ver el inventario, comprar y devolver productos. Además, el estado del inventario se guarda en un archivo JSON, lo que asegura la persistencia de los datos.

## Características
- Interfaz de comunicación cliente-servidor utilizando sockets.
- Inventario almacenado en un archivo `inventario.json`.
- Funcionalidades para:
  - Ver el inventario.
  - Comprar productos (con control de stock).
  - Devolver productos.
- Uso de hilos (threads) para manejar múltiples conexiones de clientes de manera concurrente.
- El servidor puede ser cerrado de manera controlada a través de un comando desde la consola.

## Instalación
Para ejecutar este programa, necesitas tener Python 3 instalado. 

## Uso

### Ejecutar el servidor

Primero, debes ejecutar el servidor con el siguiente comando:

```bash
python servidor.py
```

### Ejecutar el cliente
Luego, en otra terminal, ejecuta el cliente con:

```bash
python cliente.py
```

El servidor estará esperando conexiones de los clientes en el puerto 65432. El cliente puede enviar solicitudes para ver el inventario, comprar o devolver productos. Si deseas cerrar el servidor, simplemente escribe "salir" en la consola donde está corriendo el servidor.

## Funcionamiento

### Servidor

El servidor escucha conexiones entrantes de clientes.
Al recibir una solicitud, el servidor maneja las acciones como ver el inventario, comprar o devolver productos.
Utiliza hilos para manejar múltiples clientes simultáneamente sin bloquear el servicio.
El estado del inventario se guarda en el archivo inventario.json, lo que garantiza que la información se mantenga entre reinicios del servidor.

### Cliente

El cliente puede solicitar información sobre los productos disponibles en el inventario.
Puede realizar compras, las cuales son validadas por el servidor según el stock disponible.
También puede devolver productos, actualizando la cantidad disponible en el inventario.

### Hilos
El servidor utiliza hilos (threads) para manejar múltiples clientes de manera concurrente. Esto permite que varios clientes puedan interactuar con el servidor al mismo tiempo sin que se bloqueen entre ellos.


## Tecnologías utilizadas
- Python: Lenguaje principal para el desarrollo.
- Sockets: Para la comunicación entre cliente y servidor.
- JSON: Para almacenar el inventario de manera persistente.
- Hilos (Threads): Para manejar múltiples clientes simultáneamente de forma eficiente.

## Archivos importantes
- servidor.py: Código principal del servidor.
- cliente.py: Código principal del cliente.
- inventario.json: Archivo donde se guarda el inventario y sus datos.
- assets/: Carpeta con imágenes para el funcionamiento del sistema (si aplicable).
- ejemplos/: Carpeta con imágenes que muestran el funcionamiento del sistema y ejemplos de cómo se ve el proceso.


