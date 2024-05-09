import tkinter as tk

from conexidad import crear_ventana
from introduction_g import introduction_grafos


def conexidad(ventana):
    crear_ventana()
    ventana.destroy()


def introduction(ventana):
    introduction_grafos()
    ventana.destroy()


def ventana_crear():
    ventana = tk.Tk()
    ventana.title("Introducción a grafos")
    ventana.geometry("600x600")
    cabeza = tk.Label(ventana, text="Escoja la opción que más le guste")
    cabeza.pack()

    # En el comando del botón, pasa la referencia de la función 'numero' en lugar de llamarla directamente
    button = tk.Button(
        ventana, text="Dibujar grafo", command=lambda: conexidad(ventana), fg="red"
    )
    button.pack()
    button.place(x=200, y=200)
    # aqui viene el boton para abribr la ventan de introducción
    button_introdcution = tk.Button(
        ventana, text="Introducción", command=lambda: introduction(ventana), fg="red"
    )
    button_introdcution.pack()
    button_introdcution.place(x=200, y=300)
    ventana.mainloop()


ventana_crear()
