import threading
import time
import tkinter as tk

import matplotlib.pyplot as plt
import networkx as nx


def ventana_conexo():
    # Función para mostrar la ventana emergente
    ventana = tk.Tk()
    ventana.title("Grafo Conexo")
    tk.Label(
        ventana,
        text="Un grafo conexo es un grafo que de cada vertice se puede sacar un camino fundamental",
    ).pack()
    ventana.after(60000, ventana.destroy)  # Cerrar la ventana después de 1 minuto
    ventana.mainloop()


def es_conexo(G):
    if nx.is_directed(G):
        if not nx.is_weakly_connected(G):
            print("El grafo no es conexo porque no es débilmente conexo.")
            return False
    else:
        if not nx.is_connected(G):
            print("El grafo no es conexo.")
            return False

    print("El grafo es conexo.")
    return True


def dibujar_grafo():
    # Crear ventana emergente con el mensaje "Este es un grafo conexo"
    t = threading.Thread(target=ventana_conexo)
    t.start()

    # Crear un grafo vacío (dirigido o no dirigido)
    es_dirigido = input("¿Quieres un grafo dirigido? (s/n): ").lower() == "s"
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = int(input("Ingresa el número de nodos: "))
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u = int(input("Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1)))
        v = int(input("Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1)))
        G.add_edge(u, v)

        continuar = input("¿Agregar otra arista? (s/n): ").lower()
        if continuar != "s":
            break

    # Verificar si el grafo es conexo
    es_conexo(G)

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()


if __name__ == "__main__":
    dibujar_grafo()
