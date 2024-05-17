import tkinter as tk
from PIL import Image, ImageTk

from dibujar_Bipartito import dibujar_Bipartito


def ventanaBipartito(ventana):
    
    ventana = tk.Tk()
    ventana.title("Grafo Bipartito")
    ventana.geometry("500x500")
    texto = "Un grafo Bipartito es aquel que sus vertices se pueden partir en dos conjuntos disjunto\n es decir lo podemos separar en dos conjuntos de vertices que no son adyadentes entre si\n "

    label = tk.Label(ventana, text=texto)
    label.pack()

    # img_path = "images/grafosRegulares-removebg-preview(1).png"
    # img_pil = Image.open(img_path)
    # img_tk = ImageTk.PhotoImage(img_pil)
 
    # canvas = tk.Canvas(ventana, width=img_pil.width, height=img_pil.height)
    # canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    # canvas.pack()

    button = tk.Button(
        ventana, text="Dibujar grafo", command=lambda: dibujar_Bipartito(), fg="red"
    )
    button.pack()
    button.place(x=200, y=400)


    ventana.mainloop()

    return ventana