import tkinter as tk

def ventanaNoDirigido(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo No Dirigido")
    ventana.geometry("500x500")
    texto = "Un grafo no dirigido es un tipo de grafo en el cual sus aristas no constan de una dirección, lo cual permite recorrer el grafo en cualquier dirección. "
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    ventana.after(10000, ventana.destroy)
    ventana.mainloop()

    return ventana
