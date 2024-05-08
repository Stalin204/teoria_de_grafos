import tkinter as tk

import matplotlib.pyplot as plt
import networkx as nx


def definicion_grado_nodo():
    grado_no_dirigido = "El grado de un nodo en un grafo no dirigido son la cantidad de arcos (aristas ) que inciden en el nodo,en caso de que halla un loop, el arco se cuenta como entrada y salida\n"
    grafo_dirigido = "En un grafo dirigido el grado del nodo son aquellos arcos que inciden en el y los que salen de el\n "
    root = tk.Tk()

    texto = tk.Label(
        root,
        text=grado_no_dirigido + grafo_dirigido,
    )
    texto.pack()

    return


def obtener_grado_nodo(G, nodo):
    # Verificar si el nodo existe en el grafo
    if nodo in G:
        if nx.is_directed(G):
            grado_entrada = G.in_degree[nodo]
            grado_salida = G.out_degree[nodo]
            print(f"El grado de entrada del nodo {nodo} es: {grado_entrada}")
            print(f"El grado de salida del nodo {nodo} es: {grado_salida}")
        else:
            grado = G.degree[nodo]
            print(f"El grado del nodo {nodo} es: {grado}")
    else:
        print(f"El nodo {nodo} no existe en el grafo.")


def dibujar_grafo():
    definicion_grado_nodo()
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

    # Obtener el grado de un nodo
    nodo_a_consultar = int(input("Ingresa el nodo del cual deseas obtener el grado: "))
    obtener_grado_nodo(G, nodo_a_consultar)

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()


if __name__ == "__main__":
    dibujar_grafo()
