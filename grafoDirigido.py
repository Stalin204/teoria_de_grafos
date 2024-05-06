import tkinter as tk

def ventanaDirigido(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Dirigido")
    ventana.geometry("500x500")
    texto = "Un grafo dirigido es un tipo de grafo en el cual sus aristas tienen un sentido definido, es decir, una flecha que indica que va desde un vertice hacia otro. \n Significa que el grado solo puede recorrerse en la dirección que inidiquen las flechas."
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    ventana.after(10000, ventana.destroy)
    ventana.mainloop()

    return ventana
