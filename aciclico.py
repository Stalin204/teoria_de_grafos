import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)

    def es_aciclico_util(self, v, visitados, en_recorrido):
        visitados[v] = True
        en_recorrido[v] = True

        for vecino in self.grafo[v]:
            if not visitados[vecino]:
                if self.es_aciclico_util(vecino, visitados, en_recorrido):
                    return True
            elif en_recorrido[vecino]:
                return True

        en_recorrido[v] = False
        return False

    def es_aciclico(self):
        visitados = [False] * len(self.grafo)
        en_recorrido = [False] * len(self.grafo)

        for nodo in self.grafo:
            if not visitados[nodo]:
                if self.es_aciclico_util(nodo, visitados, en_recorrido):
                    return False
        return True

# Crear grafo de ejemplo
g = Grafo()
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 0)
g.agregar_arista(2, 3)
g.agregar_arista(3, 3)

# Verificar si el grafo es acíclico
if g.es_aciclico():
    print("El grafo no tiene ciclos")
else:
    print("El grafo tiene ciclos")

# Crear un objeto de grafo de NetworkX
G = nx.DiGraph()

# Agregar nodos y aristas al grafo de NetworkX
for nodo, vecinos in g.grafo.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, edge_color='k', linewidths=1, font_size=15)

# Mostrar el grafo
plt.title("Grafo")
plt.show()