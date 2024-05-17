import tkinter as tk

from setuptools import Command

from aciclico import ventanaAciclico
from bipartito import ventanaBipartito
from grado_nodo import dibujar_grafo
from grafo import ventana_queEs
from grafoDirigido import ventanaDirigido
from grafoNoDirigido import ventanaNoDirigido
from regular import ventanaRegular
from simple import ventanaSimple


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
    button_q_grafo.place(x=100, y=100)
    # grado de un nodo
    button_grado_nodo = tk.Button(
        ventana, text="Grado de un nodo", command=dibujar_grafo, fg="black"
    )
    button_grado_nodo.pack()
    button_grado_nodo.place(x=150, y=100)
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

     # Botón: Grafo Simple
    button_no_dirigido = tk.Button(
        ventana,
        text="Grafo Simple",
        command=lambda: ventanaSimple(ventana),
        fg="black",
    )
    button_no_dirigido.pack()
    button_no_dirigido.place(x=100, y=250)

    # Botón: Grafo cíclico
    button_ciclico = tk.Button(
        ventana,
        text="Grafo acíclico",
        command=lambda: ventanaAciclico(ventana),
        fg="black",
    )
    button_ciclico.pack()
    button_ciclico.place(x=100, y=300)

    # Botón: Grafo completo
    button_completo = tk.Button(ventana, text="Grafo completo")
    button_completo.pack()
    button_completo.place(x=100, y=350)

    # Botón: Grafo regular
    button_regular = tk.Button(
        ventana,
        text="Grafo regular",
        command=lambda: ventanaRegular(ventana),
        fg="black",
    )
    button_regular.pack()
    button_regular.place(x=100, y=400)

    # Botón: Grafo bipartito
    button_bipartito = tk.Button(ventana, text="Grafo bipartito", command=lambda: ventanaBipartito(ventana),fg="black")
    button_bipartito.pack()
    button_bipartito.place(x=100, y=450)

    return ventana


def grafo(ventana):
    ventana_queEs(ventana)
    ventana.destroy()


def grafoDirigido(ventana):
    ventanaDirigido(ventana)
    ventana.destroy()


def grafoNoDirigido(ventana):
    ventanaNoDirigido(ventana)
    ventana.destroy()


def grafoAciclico(ventana):
    ventanaAciclico(ventana)
    ventana.destroy()


def regular(ventana):
    ventanaRegular(ventana)
    ventana.destroy()
