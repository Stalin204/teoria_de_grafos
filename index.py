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
    ventana.title("Teoria de Grafos")
    ventana.geometry("500x500")
    titulo=tk.Label(ventana, text="Presentado por: Carlos Fabian Corrales \nJhan Carlos Martinez \nSantiago Betancourt")
    titulo.pack()
    presentado=tk.Label(ventana, text="Presnetado al docente Pedro Pablo Cardenas Alzate")
    presentado.pack()
    titulo.place(x=100, y=50)
    cabeza = tk.Label(ventana, text="Escoja una opción")
    cabeza.pack()
    cabeza.place(x=150, y=100)

    # En el comando del botón, pasa la referencia de la función 'numero' en lugar de llamarla directamente
    button = tk.Button(
        ventana, text="Conexidad", command=crear_ventana, fg="black")
    button.pack()
    button.place(x=150, y=300)
    # aqui viene el boton para abribr la ventan de introducción
    button_introdcution = tk.Button(
        ventana, text="Introducción a la teoria de grafos", command=lambda: introduction(ventana), fg="black"
    )
    button_introdcution.pack()
    button_introdcution.place(x=150, y=200)
    ventana.mainloop()


ventana_crear()
