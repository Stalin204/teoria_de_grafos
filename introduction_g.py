import tkinter as tk

from setuptools import Command

from grafoAciclico import ventanaAciclico
from grado_nodo import dibujar_grafo
from grafo import ventana_queEs
from grafoDirigido import ventanaDirigido
from grafoNoDirigido import ventanaNoDirigido
from grafoRegular import ventanaRegular
from grafoCompleto import ventanaCompleto
from grafoBipartito import ventanaBipartito
from matrices import ventanaMatrices


def introduction_grafos():
    ventana = tk.Tk()
    ventana.geometry("600x600")

    # Botón: ¿Qué es un grafo?
    button_q_grafo = tk.Button(
        ventana,
        text="¿Qué es un grafo?",
        command=lambda: ventana_queEs(ventana),
        fg="black",
    )
    button_q_grafo.pack()
    button_q_grafo.place(x=200, y=100)

    # Botón: Grafo dirigido
    button_dirigido = tk.Button(
        ventana,
        text="Grafo dirigido",
        command=lambda: ventanaDirigido(ventana),
        fg="black",
    )
    button_dirigido.pack()
    button_dirigido.place(x=100, y=150)

    # Botón: Grafo no dirigido
    button_no_dirigido = tk.Button(
        ventana,
        text="Grafo no dirigido",
        command=lambda: ventanaNoDirigido(ventana),
        fg="black",
    )
    button_no_dirigido.pack()
    button_no_dirigido.place(x=100, y=200)

    # Botón: Grafo cíclico
    button_ciclico = tk.Button(
        ventana,
        text="Grafo acíclico",
        command=lambda: ventanaAciclico(ventana),
        fg="black",
    )
    button_ciclico.pack()
    button_ciclico.place(x=100, y=250)

    # Botón: Grafo completo
    button_completo = tk.Button(
        ventana, 
        text="Grafo completo",
        command=lambda: ventanaCompleto(ventana),
        fg="black",
    )
    button_completo.pack()
    button_completo.place(x=100, y=300)

    # Botón: Grafo regular
    button_regular = tk.Button(
        ventana,
        text="Grafo regular",
        command=lambda: ventanaRegular(ventana),
        fg="black",
    )
    button_regular.pack()
    button_regular.place(x=300, y=200)

    # Botón: Grafo bipartito
    button_bipartito = tk.Button(
        ventana, 
        text="Grafo bipartito",
        command=lambda: ventanaBipartito(ventana),
        fg="black",
        )
    button_bipartito.pack()
    button_bipartito.place(x=300, y=250)

    # grado de un nodo
    button_grado_nodo = tk.Button(
        ventana, text="Grado de un nodo", command=dibujar_grafo, fg="black"
    )
    button_grado_nodo.pack()
    button_grado_nodo.place(x=300, y=150)

    #matrices
    button_matrices=tk.Button(
        ventana, 
        text="Matrices de Adyacencia e Incidencia", 
        command=lambda: ventanaMatrices(ventana), 
        fg="black")
    button_matrices.pack()
    button_matrices.place(x=100, y=350)
    return ventana


