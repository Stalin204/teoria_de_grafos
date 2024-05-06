import tkinter as tk

def ventana_queEs(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("¿Que es un grafo?")
    ventana.geometry("500x500")
    texto = "Un grafo es una composición entre un conjunto de vértices o nodos y un conjunto de aristas o arcos de la forma G(V,A) \n Los vertices son representados como puntos y las aristas como una linea que conecta dos nodos."
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    ventana.after(10000, ventana.destroy)
    ventana.mainloop()

    return ventana

