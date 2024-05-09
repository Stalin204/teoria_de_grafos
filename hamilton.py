import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Crear una ventana con dos subfiguras
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax2.axis("off")


def esHamiltoniano(G):
    # Verificamos si es dirigido o no
    if nx.is_directed(G):
        #verificamos si el grafo tiene conexidad debil
        if nx.is_weakly_connected(G):

            text = "El grafo no es Hamiltoniano\n ni tiene camino Hamiltoniano \nporque es débilmente conexo"
            ax2.text(0.5, 0.5, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            return False
    else:
        # verificamos si el grafo es conexo
        if not nx.is_connected(G):
           
            #ponemos el texto en la segunda figura "ax2"
            text = "El grafo no es Hamiltoniano \n ni tiene un camino Hamiltoniano \nporque no es conexo"
            ax2.text(0.5, 0.5, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            
            return False
        n = G.number_of_nodes()
        #Agrego el texto
        text = "según el teorema de Dirac\n si G es conexo y cada vertice 'v' de G \n cumple que deg(v)>=|V|/2\n su grado es mayor o igual al total de vertices dividido entre dos\nEl grafo es Hamiltoniano"
        ax2.text(0.5, 1, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            
        # verificamos si se cumple el teorema de Dirac
        if all(deg >= n / 2 for _, deg in G.degree()):
            
            text = "El grafo es Hamiltoniano\n porque cumple el teorema de Dirac"
            ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            return True
        else:
            
            text = "El grafo no es Hamiltoniano\n porque no cumple el teorema de Dirac"
            ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)
            return False
    

def caminoHamiltoniano(G):
    n = len(G)
    visitado = [False] * n
    camino = []

    def recorrer(node):
        visitado[node] = True
        camino.append(node)

        if len(camino) == n:
            return True
        

        for vecino in G[node]:
            if not visitado[vecino]:
                if recorrer(vecino):
                    return True

        visitado[node] = False
        camino.pop()
        return False

    for node in range(n):
        if recorrer(node):
            return True

    return False

def dibujar_grafo_hamilton():

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

    # Opciones para el usuario
    opcion = input(
        "¿Qué deseas verificar?\n1. Si es Hamiltoniano.\n2. Si tiene un camino Hamiltoniano.\nSelecciona una opción (1/2): "
    )

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    #creamos el grafo en ax1
    nx.draw(G, pos,ax=ax1,with_labels=True, node_size=500, node_color="skyblue", font_size=10)


    if opcion == "1":
        esHamiltoniano(G)
    elif opcion == "2":
        nx.draw_networkx_edges(G, pos,ax=ax1, width=2, alpha=0.5, edge_color="r")
        if caminoHamiltoniano(G):
            text = "El grafo tiene un camino Hamiltoniano"
        else:
            text ="El grafo no tiene un camino Hamiltoniano"
        ax2.text(0.5, 0.4, text, transform=ax2.transAxes,  ha="center", va="top", fontsize=12)    
    plt.show()


if __name__ == "__main__":
    dibujar_grafo_hamilton()
