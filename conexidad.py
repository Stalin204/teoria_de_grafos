import tkinter as tk

from matplotlib.pyplot import text

from hamilton import dibujar_grafo_hamilton
from konisberg import difinicion_puentes_konisber
from ventana_euler import crear_ventana_euler


def euler_ventana_grafo(ventana):
    crear_ventana_euler()
    ventana.destroy()


def crear_ventana():
    ventana = tk.Tk()  # Llama al constructor Tk() para crear la ventana
    ventana.title("Conexidad")  # Proporciona un título entre las comillas
    ventana.geometry("500x500")  # tamaño de la ventana
    buttoneuler = tk.Button(
        ventana, text="grafo euleriano", command=lambda: euler_ventana_grafo(ventana)
    )
    buttoneuler.pack()
    buttoneuler.place(x=200, y=200)
    # aui debe de ir el boton para el grafo hamiltoniano
    button_hamilton = tk.Button(
        ventana, text="grafo hamiltoniano", command=dibujar_grafo_hamilton
    )
    button_hamilton.pack()
    button_hamilton.place(x=200, y=250)
    # va la función de konisberg
    button_koonisber = tk.Button(
        ventana, text="puentes de konisberg", command=difinicion_puentes_konisber
    )
    button_koonisber.pack()
    button_koonisber.place(x=200, y=300)

    return ventana
