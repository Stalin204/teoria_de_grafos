import tkinter as tk

def ventana_queEs(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("¿Que es un grafo")
    ventana.geometry("500x500")
    tk.Label(
        ventana,
        text="Un grafo es una composición entre un conjunto de vertices o nodos y un conjunto de aristas o arcos de la forma G(V,A)"
    ).pack()
    button = tk.Button(
        ventana, text="Regresar", command=lambda: index(ventana), fg="black"
    )
    button.pack()
    button.place(x=200, y=200)
    ventana.mainloop()

