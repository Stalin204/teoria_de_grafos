import matplotlib.pyplot as plt
import networkx as nx

def esHamiltoniano(G):
    #Verificamos si es dirigido o no
    if nx.is_directed(G):
        #verificamos si el grafo tiene conexidad debil
        if nx.is_weakly_connected(G):
            print("El grafo no es Hamiltoniano ni tiene camino Hamiltoniano porque es débilmente conexo.")
            return False
    else:
        #verificamos si el grafo es conexo
        if not nx.is_connected(G):
            print("El grafo no es Hamiltoniano ni tiene un camino Hamiltoniano porque no es conexo")
            return False
        n=G.number_of_nodes()
        
        print("según el teorema de Dirac si G es conexo y cada vertice(v) de G cumple que deg(v)>=|V|/2\nEl grafo es Hamiltoniano")
        #verificamos si se cumple el teorema de Dirac
        if all(deg >= n/2 for _,deg in G.degree()):
            print("El grafo es Hamiltoniano porque cumple el teorema de Dirac")
            return True
        else:
            print("el grafo no es Hamiltoniano porque no cumple el teorema de Dirac")
            return False  

 

def dibujar_grafo():
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
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)

    if opcion == "1":
        esHamiltoniano(G)
    elif opcion == "2":
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color="r")
        esHamiltoniano(G)

    plt.show()


if __name__ == "__main__":
    dibujar_grafo()


    
    
