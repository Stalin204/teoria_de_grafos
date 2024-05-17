import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog,messagebox
import matplotlib.pyplot as plt
import networkx as nx

def comprobarIgualdad(G,ax2):
    if all(deg == G.degree(0) for _, deg in G.degree):
        text="El Grafo es Regular\n por que el grado de todos sus nodos es igual = "+ str(G.degree(0))
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
        return True
    else:
        text="El Grafo No es Regular\n por que el grado de todos sus nodos no son iguales \n lista=[(numero del nodo, el grado del nodo),] \n lista = "+ str(list(G.degree()))
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
        return False
    


def dibujar_Regular():

    # Crear una ventana con dos subfiguras
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    #quitamos el grafico generado automaticamente
    ax2.axis("off")
    
    es_dirigido = messagebox.askyesno(
        "Tipo de grafo", "¿Quieres un grafo dirigido? (s/n):"
    )
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Nodos","ingresa el numero de nodos:")
    if num_nodos is None:
        return
    
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u=simpledialog.askinteger("Aristas","Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1))
        v=simpledialog.askinteger("Aristas","Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1))
        
        G.add_edge(u, v)
        
        continuar = messagebox.askyesno(
        "Arista", "¿Quieres otra arista? (s/n):"
    )
        if not continuar:
            break

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    #creamos el grafo en ax1
    nx.draw(G, pos,ax=ax1,with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    
    
    if comprobarIgualdad(G,ax2):
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        
    else:
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        
    plt.show()