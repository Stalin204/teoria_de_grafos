import tkinter as tk

def ventanaRegular(ventana):
    #Funcion para mostrar que es un grafo
    ventana=tk.Tk()
    ventana.title("Grafo Regular")
    ventana.geometry("500x500")
    texto = "Un grafo Regular es aquel que todos los grados de sus nodos o vertices son iguales"
    
    # Crear el Label con el texto ajustado al tamaño de la ventana
    label = tk.Label(ventana, text=texto, wraplength=480)  # El wraplength define el ancho máximo antes de saltar de línea
    label.pack()
    ventana.after(10000, ventana.destroy)
    ventana.mainloop()

    return ventana