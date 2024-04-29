import tkinter as tk

from euler import dibujar_grafo


def crear_ventana():
    ventana = tk.Tk()  # Llama al constructor Tk() para crear la ventana
    ventana.title("Conexidad")  # Proporciona un título entre las comillas
    ventana.geometry("500x500")  # tamaño de la ventana
    buttoneuler = tk.Button(ventana, text="grafo euleriano", command=dibujar_grafo)
    buttoneuler.pack()
    buttoneuler.place(x=200, y=200)
    return ventana
