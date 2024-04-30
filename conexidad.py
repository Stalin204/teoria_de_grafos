import tkinter as tk

from matplotlib.pyplot import text

from euler import dibujar_grafo


def crear_ventana():
    ventana = tk.Tk()  # Llama al constructor Tk() para crear la ventana
    ventana.title("Conexidad")  # Proporciona un título entre las comillas
    ventana.geometry("500x500")  # tamaño de la ventana
    buttoneuler = tk.Button(ventana, text="grafo euleriano", command=dibujar_grafo)
    buttoneuler.pack()
    buttoneuler.place(x=200, y=200)
    # aui debe de ir el boton para el grafo hamiltoniano
    button_hamilton = tk.Button(ventana, text="grafo hamiltoniano")
    button_hamilton.pack()
    button_hamilton.place(x=200, y=250)
    # va la función de konisberg
    button_koonisber = tk.Button(ventana, text="puentes de konisberg")
    button_koonisber.pack()
    button_koonisber.place(x=200, y=300)
    # va la función del terema de dirac
    button_dirac = tk.Button(ventana, text="teorema de dirac")
    button_dirac.pack()
    button_dirac.place(x=200, y=350)

    return ventana
