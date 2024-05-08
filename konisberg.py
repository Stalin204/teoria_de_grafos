import tkinter as tk


def difinicion_puentes_konisber():
    parte1 = "Lso puentes de konisberg fueron un problema matemático que se planteó en el siglo XVIII y que fue resuelto por Leonhard Euler en 1735.\n El problema consiste en determinar si es posible recorrer todos los puentes de la ciudad de Konisberg, cruzando cada uno de ellos una sola vez y volviendo al punto de partida.\n La ciudad de Konisberg estaba dividida en cuatro zonas por el río Pregel y siete puentes la unían.\n El problema consistía en determinar si era posible recorrer todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez.\n Euler demostró que esto no era posible y que, por lo tanto, no existía un camino que recorriera todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez.\n"
    parte2 = "para resolver el problema, Euler representó la ciudad de Konisberg como un grafo, es decir, un conjunto de nodos (las zonas de la ciudad) y aristas (los puentes que las unen).\n En este grafo, cada nodo representa una zona de la ciudad y cada arista representa un puente.\n Euler demostró que, para que exista un camino que recorra todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez, es necesario que todos los nodos del grafo tengan un número par de aristas que los unan.\n En el caso de la ciudad de Konisberg, dos de los nodos tenían un número impar de aristas que los unían, por lo que no era posible recorrer todos los puentes de la ciudad sin cruzar ninguno de ellos más de una vez.\n"
    window = tk.Tk()
    window.title("Definición de puentes de Konisberg")
    window.geometry("400x400")

    label = tk.Label(window, text=parte1 + parte2)
    label.pack()

    label = tk.Label(
        window, text="Un puente de Konisberg es un grafo que tiene 4 nodos y 7 aristas"
    )
    label.pack()

    window.mainloop()


difinicion_puentes_konisber()
