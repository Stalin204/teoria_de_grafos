import tkinter as tk

from conexidad import crear_ventana


def conexidad(ventana):
    crear_ventana()
    ventana.destroy()


def ventana_crear():
    ventana = tk.Tk()
    ventana.title("Introducción a grafos")
    ventana.geometry("600x600")
    cabeza = tk.Label(ventana, text="Escoja la opción que más le guste").pack()

    # En el comando del botón, pasa la referencia de la función 'numero' en lugar de llamarla directamente
    button = tk.Button(
        ventana, text="Dibujar grafo", command=lambda: conexidad(ventana), fg="red"
    )
    button.pack()
    button.place(x=200, y=200)

    ventana.mainloop()


ventana_crear()
