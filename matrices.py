import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

def ventanaMatrices(ventana):
    ventana = tk.Tk()
    ventana.title("Matrices")
    ventana.geometry("500x500")
    
    # Título: Matriz de adyacencia
    titulo_adyacencia = tk.Label(ventana, text="Matriz de adyacencia", font=("Arial", 14, "bold"))
    titulo_adyacencia.pack()

    # Label: Definición de la matriz de adyacencia
    definicion_adyacencia = tk.Label(ventana, text="La matriz de adyacencia representa las conexiones entre los nodos del grafo. Si el elemento (i, j) es 1, indica que hay una arista entre los nodos i y j; si es 0, indica que no hay arista.", wraplength=480)
    definicion_adyacencia.pack()

    # Título: Matriz de incidencia
    titulo_incidencia = tk.Label(ventana, text="Matriz de incidencia", font=("Arial", 14, "bold"))
    titulo_incidencia.pack()

    # Label: Definición de la matriz de incidencia
    definicion_incidencia = tk.Label(ventana, text="La matriz de incidencia es una forma de representar un grafo donde cada fila representa un nodo y cada columna representa una arista. Si el elemento (i, j) es 1, indica que el nodo i es un punto final de la arista j; si es -1, indica que el nodo i es el inicio de la arista j; si es 0, indica que el nodo i no está conectado a la arista j.", wraplength=480)
    definicion_incidencia.pack()

    # Botón para dibujar el grafo
    button_dibujar = tk.Button(ventana, text="Dibujar Grafo", command=dibujarGrafo, fg="black")
    button_dibujar.pack()

    ventana.mainloop()

def dibujarGrafo():
    es_dirigido = simpledialog.askstring("Tipo de grafo", "¿Quieres un grafo dirigido? (s/n): ")
    if es_dirigido is not None:
        es_dirigido = es_dirigido.lower() == "s"
    else:
        # Si el usuario no ingresa ninguna respuesta, asumimos un valor predeterminado (False)
        es_dirigido = False
    G = nx.DiGraph() if es_dirigido else nx.Graph()

    # Agregar nodos
    num_nodos = simpledialog.askinteger("Número de nodos", "Ingresa el número de nodos:")
    if num_nodos is None:  # Si se cancela el diálogo, salir de la función
        return
    
    for i in range(num_nodos):
        G.add_node(i)

    # Agregar aristas (enlaces)
    while True:
        u = simpledialog.askinteger("Arista", f"Ingresa el nodo de origen (0-{num_nodos - 1}):")
        v = simpledialog.askinteger("Arista", f"Ingresa el nodo de destino (0-{num_nodos - 1}):")
        if u is None or v is None:  # Si se cancela el diálogo, salir del bucle
            break
        G.add_edge(u, v)

        continuar = simpledialog.askstring("Agregar otra arista", "¿Agregar otra arista? (s/n):")
        if continuar is None or continuar.lower() != "s":  # Si se cancela el diálogo o el usuario ingresa algo que no es "s", salir del bucle
            break
    # Dibujar el grafo
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)

    # Mostrar el grafo
    plt.title("Grafo")
    plt.show()
    matriz_frame = tk.Tk()
    matriz_frame.title("Matrices")

    # Matriz de adyacencia
    matriz_adyacencia = nx.adjacency_matrix(G)
    matriz_adyacencia_label = tk.Label(matriz_frame, text="Matriz de adyacencia:", font=("Arial", 12, "bold"))
    matriz_adyacencia_label.pack()
    matriz_adyacencia_text = tk.Text(matriz_frame, height=6, width=40)
    matriz_adyacencia_text.insert(tk.END, str(matriz_adyacencia.todense()))
    matriz_adyacencia_text.pack()

    # Matriz de incidencia
    matriz_incidencia = nx.incidence_matrix(G, oriented=True)
    matriz_incidencia_label = tk.Label(matriz_frame, text="Matriz de incidencia:", font=("Arial", 12, "bold"))
    matriz_incidencia_label.pack()
    matriz_incidencia_text = tk.Text(matriz_frame, height=6, width=40)
    matriz_incidencia_text.insert(tk.END, str(matriz_incidencia.todense()))
    matriz_incidencia_text.pack()

    matriz_frame.mainloop()

    