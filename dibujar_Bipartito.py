import tkinter as tk
from PIL import Image, ImageTk
from tkinter import simpledialog,messagebox
import matplotlib.pyplot as plt
import networkx as nx

def comprobarBipartito(G):
    n=len(G)
    visitado= [False]*n
    camino=[]

    def recorrer(node,nodeinicio):
        visitado[node]=True
        camino.append(node)
        
        for vecino in G[node]:
            if not visitado[vecino]:
                if recorrer(vecino,nodeinicio):
                    return True         
                           
        for v in range(n):
            if visitado[v] == False:
                if recorrer(v,v):
                    return True
                
        
        for vecino in G[node]:
            if vecino==nodeinicio:
                if len(camino)%2!=0:
                    return False
                else:
                    return True
                
    if recorrer(0,0):
        return True
    else:    
        return False

def dibujar_Bipartito():

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
    
    
    if comprobarBipartito(G):
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        text="El grafo es Bipartito"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
    else:
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        text="El grafo no es Bipartito"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
        
    plt.show()
