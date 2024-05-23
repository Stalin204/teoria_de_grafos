import tkinter as tk

from hamilton import dibujar_grafo_hamilton
from konisberg import difinicion_puentes_konisber
from ventana_euler import crear_ventana_euler


def euler_ventana_grafo(ventana):
    crear_ventana_euler()


def crear_ventana():
    ventana = tk.Tk()  # Llama al constructor Tk() para crear la ventana
    ventana.title("Conexidad")  # Proporciona un título entre las comillas
    ventana.geometry("500x500")  # tamaño de la ventana

    # Estilo de fuente
    font = ("Helvetica", 12)

    # Estilo de los botones
    button_style = {
        "font": font,
        "bg": "#4CAF50",  # Verde
        "fg": "white",    # Texto blanco
        "relief": "raised",
        "borderwidth": 3,
        "width": 15,
        "height": 2,
    }

    # Título
    title_label = tk.Label(ventana, text="Seleccione una opción:", font=("Helvetica", 16))
    title_label.pack(pady=20)

    buttoneuler = tk.Button(
        ventana, text="Grafo Euleriano", command=lambda: euler_ventana_grafo(ventana), **button_style
    )
    buttoneuler.pack(pady=10)

    button_hamilton = tk.Button(
        ventana, text="Grafo Hamiltoniano", command=dibujar_grafo_hamilton, **button_style
    )
    button_hamilton.pack(pady=10)

    button_koonisber = tk.Button(
        ventana, text="Puentes de Konisberg", command=difinicion_puentes_konisber, **button_style
    )
    button_koonisber.pack(pady=10)

    return ventana

crear_ventana().mainloop()
