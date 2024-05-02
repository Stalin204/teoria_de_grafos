import tkinter as tk
from grafo import ventana_queEs

def introduction_grafos():
    ventana = tk.Tk()
    ventana.geometry("600x600")
    # viene la explicacipon de lo que es un grafo
    button_q_grafo = tk.Button(ventana, text="¿Qué es un grafo?", command=lambda: ventana_queEs(ventana),fg="black")
    button_q_grafo.pack()
    button_q_grafo.place(x=100, y=100)
    # grafo dirigido
    button_dirigido = tk.Button(ventana, text="Grafo dirigido")
    button_dirigido.pack()
    button_dirigido.place(x=100, y=150)
    # grafo no dirigido
    button_no_dirigido = tk.Button(ventana, text="Grafo no dirigido")
    button_no_dirigido.pack()
    button_no_dirigido.place(x=100, y=200)
    # grafo ciclico
    button_ciclico = tk.Button(ventana, text="Grafo ciclico")
    button_ciclico.pack()
    button_ciclico.place(x=200, y=350)
    # grafo comoleto
    button_completo = tk.Button(ventana, text="Grafo completo")
    button_completo.pack()
    button_completo.place(x=200, y=400)
    # grafo regular
    button_regular = tk.Button(ventana, text="Grafo regular")
    button_regular.pack()
    button_regular.place(x=200, y=450)
    # grafo bipartito
    button_bipartito = tk.Button(ventana, text="Grafo bipartito")
    button_bipartito.pack()
    button_bipartito.place(x=200, y=500)
    return ventana

def grafo(ventana):
    ventana_queEs(ventana)
    ventana.destroy()
