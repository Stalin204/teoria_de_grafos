import tkinter as tk
from tkinter import font

from conexidad import crear_ventana
from introduction_g import introduction_grafos


def conexidad(ventana):
    crear_ventana()


def introduction(ventana):
    introduction_grafos()


def ventana_crear():
    ventana = tk.Tk()
    ventana.title("Teoría de Grafos")
    ventana.geometry("600x500")
    ventana.configure(bg="#f0f0f0")  # Fondo gris claro

    # Fuente personalizada
    font_title = font.Font(family="Helvetica", size=14, weight="bold")
    font_body = font.Font(family="Helvetica", size=12)

    titulo = tk.Label(
        ventana, 
        text="Presentado por:\nCarlos Fabian Corrales\nJhan Carlos Martinez\nSantiago Betancourt",
        font=font_title,
        bg="#f0f0f0",
        fg="#333333"
    )
    titulo.pack(pady=20)  # Espacio superior e inferior

    presentado = tk.Label(
        ventana, 
        text="Presentado al docente Pedro Pablo Cardenas Alzate. Ph.D",
        font=font_body,
        bg="#f0f0f0",
        fg="#333333"
    )
    presentado.pack(pady=10)

    cabeza = tk.Label(
        ventana, 
        text="Escoja una opción", 
        font=font_title,
        bg="#f0f0f0",
        fg="#333333"
    )
    cabeza.pack(pady=30)

    button_style = {
        "font": font_body,
        "bg": "#4caf50",  # Verde
        "fg": "white",
        "activebackground": "#45a049",
        "activeforeground": "white",
        "width": 30,
        "height": 2,
        "bd": 2,
        "relief": "raised"
    }

    button_introdcution = tk.Button(
        ventana, 
        text="Introducción a la teoría de grafos", 
        command=lambda: introduction(ventana), 
        **button_style
    )
    button_introdcution.pack(pady=10)

    button_conexidad = tk.Button(
        ventana, 
        text="Conexidad", 
        command=lambda: conexidad(ventana), 
        **button_style
    )
    button_conexidad.pack(pady=10)

    ventana.mainloop()


ventana_crear()
