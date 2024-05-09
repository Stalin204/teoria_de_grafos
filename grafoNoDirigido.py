import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx

def ventanaNoDirigido(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo No Dirigido")
    ventana.geometry("500x500")
    texto = "Un grafo no dirigido es un tipo de grafo en el cual sus aristas no constan de una dirección, lo cual permite recorrer el grafo en cualquier dirección. "
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    button_dibujar=tk.Button(ventana, text="Dibujar grafo No Dirigido", command=dibujar_grafoNoDirigido, fg="black")
    button_dibujar.pack()
    button_dibujar.place(x=100, y=100)
    ventana.mainloop()
    return ventana


def dibujar_grafoNoDirigido():
    g=nx.MultiGraph()
    # Agregar nodos
    num_nodos = int(input("Ingresa el número de nodos: "))
    for i in range(num_nodos):
        g.add_node(i)

         # Agregar aristas (enlaces)
    while True:
        u = int(input("Ingresa el nodo de origen (0-{0}): ".format(num_nodos - 1)))
        v = int(input("Ingresa el nodo de destino (0-{0}): ".format(num_nodos - 1)))
        g.add_edge(u, v)

        continuar = input("¿Agregar otra arista? (s/n): ").lower()
        if continuar != "s":
            break

    # Dibujar el grafo
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)
    plt.show()

