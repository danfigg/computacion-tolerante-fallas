# Blackjack con Estado Persistente

Este es un juego de Blackjack con una interfaz gráfica en **Tkinter**, que permite guardar y restaurar el estado de ejecución utilizando **pickle** y un manejador de archivos con **contextlib**.

## Características

- Interfaz gráfica con **Tkinter**.
- Almacena el estado de la partida con **pickle**.
- Carga el juego guardado si existe un estado previo.
- Simulación del juego de Blackjack con reglas básicas.

## Instalación

Para ejecutar este programa, necesitas tener **Python 3** instalado junto con los siguientes paquetes:

```bash
pip install pillow
```

## Uso

Ejecuta el script con:

```bash
python blackjack.py
```

Si hay una partida guardada, el programa te preguntará si deseas continuarla.

## Funcionamiento

1. Se inicializa la baraja y se reparten cartas al jugador y al dealer.
2. El jugador puede:
   - **Pedir carta**: Agrega una carta a su mano.
   - **Plantarse**: Mantiene su puntaje y deja que el dealer juegue.
3. Si el puntaje del jugador supera 21, pierde automáticamente.
4. El dealer juega hasta alcanzar un puntaje mínimo de 17.
5. Se comparan los puntajes para determinar al ganador.
6. El estado de la partida se guarda en un archivo si el usuario lo elige.

## Tecnologías utilizadas

- **Python**: Lenguaje principal.
- **Tkinter**: Interfaz gráfica.
- **Pickle**: Para guardar y restaurar el estado.
- **Contextlib**: Manejador de archivos seguro.
- **Pillow**: Para mostrar imágenes de cartas.

## Archivos importantes

- `blackjack.py`: Código principal del juego.
- `blackjack_save.txt`: Archivo donde se guarda el estado de la partida.
- `assets/`: Carpeta con las imágenes de las cartas.
-  `ejemplos/`: Capturas del funcionamiento del programa


