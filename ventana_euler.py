import tkinter as tk

import matplotlib.pyplot as plt
import networkx as nx


def introduccion_grafo_euleriano():
    parte1 = "Un circuito euleriano es un circuito simple que recorre todas las aristas del grafo"
    parte2 = "un grafo que admite un circuito euleriano se llama grafo euleriano"
    parte3 = "Un grafo euleriano es aquel grafo que permite recorrer todas sus aristas una sola vez y regresar al punto de partida"
    parte4 = "Un grafo conexo es euleriano si y solo si todos sus vértices son de grado par\n"
    return parte1 + "\n" + parte2 + "\n" + parte3 + "\n" + parte4


def introduccion_camino_euleriano():
    texto = "UN camino eulerinaoi es un camino simple que recorre todas las aristas del grafo\n"
    parte1 = "Un grafo no eulerinao es que permite un camino euleriano se llama semi-euleriano\n"
    texto = texto + parte1
    return texto


def ventanas_grafos_eulerianos():
    ventana = tk.Tk()

    # Título para la sección de introducción al Grafo Euleriano
    titulo_grafo_euleriano = tk.Label(
        ventana, text="Introducción al Grafo Euleriano", font=("Arial", 14, "bold")
    )
    titulo_grafo_euleriano.pack()

    # Contenido para la sección de introducción al Grafo Euleriano
    parte_1_grafo_euleriano = tk.Label(
        ventana, text=introduccion_grafo_euleriano(), font=("Arial", 12)
    )
    parte_1_grafo_euleriano.pack()

    # Imagen para la sección de introducción al Grafo Euleriano
    # imagen_1 = Image.open("imagen_grafo_euleriano.png")
    # imagen_1 = imagen_1.resize((200, 200), Image.ANTIALIAS)
    # imagen_1 = ImageTk.PhotoImage(imagen_1)
    # label_imagen_1 = tk.Label(ventana, image=imagen_1)
    # label_imagen_1.pack()

    # Título para la sección de introducción al Camino Euleriano
    titulo_camino_euleriano = tk.Label(
        ventana, text="Introducción al Camino Euleriano", font=("Arial", 14, "bold")
    )
    titulo_camino_euleriano.pack()

    # Contenido para la sección de introducción al Camino Euleriano
    parte_2_camino_euleriano = tk.Label(
        ventana, text=introduccion_camino_euleriano(), font=("Arial", 12)
    )
    parte_2_camino_euleriano.pack()

    # Imagen para la sección de introducción al Camino Euleriano
    # imagen_2 = Image.open("imagen_camino_euleriano.png")
    # imagen_2 = imagen_2.resize((200, 200), Image.ANTIALIAS)
    # imagen_2 = ImageTk.PhotoImage(imagen_2)
    # label_imagen_2 = tk.Label(ventana, image=imagen_2)
    # label_imagen_2.pack()

    return ventana


def es_euleriano(G):
    if nx.is_directed(G):
        if not nx.is_weakly_connected(G):
            print(
                "El grafo no es euleriano ni tiene camino euleriano porque no es débilmente conexo."
            )
            return False
    else:
        if not nx.is_connected(G):
            print(
                "El grafo no es euleriano ni tiene camino euleriano porque no es conexo."
            )
            return False

    num_impares = sum(deg % 2 != 0 for _, deg in G.degree)
    if num_impares == 0:
        print("El grafo es euleriano.")
        return True
    elif num_impares == 2:
        print("El grafo tiene un camino euleriano.")
        return True
    else:
        print("El grafo no es euleriano ni tiene camino euleriano.")
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
        "¿Qué deseas verificar?\n1. Si es euleriano.\n2. Si tiene un camino euleriano.\nSelecciona una opción (1/2): "
    )

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10)

    if opcion == "1":
        es_euleriano(G)
    elif opcion == "2":
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color="r")
        es_euleriano(G)

    plt.show()


def crear_ventana_euler():
    windwos = tk.Tk()
    label_titulo = tk.Label(windwos, text="Introcudción grafos y ciclos eulerianos")
    label_titulo.pack()
    button_introducion_ciclos_eulerrianos = tk.Button(
        windwos,
        text="Introducción a los ciclos eulerianos",
        command=ventanas_grafos_eulerianos,
    )
    button_introducion_ciclos_eulerrianos.pack()
    button_introducion_ciclos_eulerrianos.place()

    button_grafo_eulerinao = tk.Button(
        windwos, text="Grafo euleriano", command=dibujar_grafo
    )
    button_grafo_eulerinao.pack()
    button_grafo_eulerinao.place()
    return windwos
