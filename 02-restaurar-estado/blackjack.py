import random
import pickle
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from contextlib import contextmanager

SAVE_FILE = "blackjack_save.txt"

CARTAS = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
TIPOS = ['C', 'D', 'H', 'S']
BARAJA = [f"{numero}{tipo}" for numero in CARTAS for tipo in TIPOS] * 4

@contextmanager
def manejar_archivo(nombre_archivo, modo):
    archivo = None
    try:
        archivo = open(nombre_archivo, modo)
        yield archivo
    finally:
        if archivo:
            archivo.close()

def guardar_estado(estado):
    with manejar_archivo(SAVE_FILE, "wb") as file:
        pickle.dump(estado, file)

def cargar_estado():
    if os.path.exists(SAVE_FILE):
        with manejar_archivo(SAVE_FILE, "rb") as file:
            return pickle.load(file)
    return None

def calcular_puntaje(mano):
    total = sum(CARTAS[carta[:-1]] for carta in mano)
    ases = sum(1 for carta in mano if carta[:-1] == 'A')
    
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    
    return total

def repartir_carta(mano):
    carta = random.choice(BARAJA)
    mano.append(carta)
    return carta

def actualizar_interfaz():
    for widget in frame_jugador.winfo_children():
        widget.destroy()
    for widget in frame_dealer.winfo_children():
        widget.destroy()

    for carta in mano_jugador:
        img = Image.open(f"assets/{carta}.png")
        img = img.resize((100, 150))
        img = ImageTk.PhotoImage(img)
        lbl = tk.Label(frame_jugador, image=img)
        lbl.image = img
        lbl.pack(side="left")

    for carta in mano_dealer:
        img = Image.open(f"assets/{carta}.png")
        img = img.resize((100, 150))
        img = ImageTk.PhotoImage(img)
        lbl = tk.Label(frame_dealer, image=img)
        lbl.image = img
        lbl.pack(side="left")

    lbl_puntaje_jugador.config(text=f"Tu puntaje: {calcular_puntaje(mano_jugador)}")
    lbl_puntaje_dealer.config(text=f"Puntaje del dealer: {calcular_puntaje(mano_dealer)}")

def pedir():
    repartir_carta(mano_jugador)
    actualizar_interfaz()
    
    if calcular_puntaje(mano_jugador) > 21:
        messagebox.showinfo("Fin del Juego", "Te pasaste de 21. Has perdido.")
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)

def plantarse():
    while calcular_puntaje(mano_dealer) < 17:
        repartir_carta(mano_dealer)
    
    actualizar_interfaz()

    puntaje_jugador = calcular_puntaje(mano_jugador)
    puntaje_dealer = calcular_puntaje(mano_dealer)

    if puntaje_dealer > 21 or puntaje_jugador > puntaje_dealer:
        resultado = "¡Ganaste!"
    elif puntaje_jugador < puntaje_dealer:
        resultado = "Perdiste."
    else:
        resultado = "Empate."

    messagebox.showinfo("Resultado", resultado)

def guardar_y_salir():
    guardar_estado((mano_jugador, mano_dealer))
    messagebox.showinfo("Guardado", "Juego guardado. ¡Hasta la próxima!")
    root.quit()

def jugar_de_nuevo():
    global mano_jugador, mano_dealer
    mano_jugador, mano_dealer = [], []
    repartir_carta(mano_jugador)
    repartir_carta(mano_jugador)
    repartir_carta(mano_dealer)
    repartir_carta(mano_dealer)
    actualizar_interfaz()

estado = cargar_estado()
if estado:
    if messagebox.askyesno("Juego guardado", "Se encontró una partida guardada. ¿Quieres continuar?"):
        mano_jugador, mano_dealer = estado
    else:
        mano_jugador, mano_dealer = [], []
else:
    mano_jugador, mano_dealer = [], []

if not mano_jugador:
    repartir_carta(mano_jugador)
    repartir_carta(mano_jugador)
    repartir_carta(mano_dealer)
    repartir_carta(mano_dealer)

root = tk.Tk()
root.title("Blackjack")
root.geometry("600x550")

frame_jugador = tk.Frame(root)
frame_jugador.pack(pady=10)
lbl_puntaje_jugador = tk.Label(root, text="")
lbl_puntaje_jugador.pack()

frame_dealer = tk.Frame(root)
frame_dealer.pack(pady=10)
lbl_puntaje_dealer = tk.Label(root, text="")
lbl_puntaje_dealer.pack()

btn_pedir = tk.Button(root, text="Pedir Carta", command=pedir) 
btn_pedir.pack(pady=5)

btn_plantarse = tk.Button(root, text="Plantarse", command=plantarse)
btn_plantarse.pack(pady=5)

btn_guardar = tk.Button(root, text="Guardar y Salir", command=guardar_y_salir)
btn_guardar.pack(pady=5)

btn_jugar_de_nuevo = tk.Button(root, text="Jugar de Nuevo", command=jugar_de_nuevo)
btn_jugar_de_nuevo.pack(pady=5)

actualizar_interfaz()

root.mainloop()
