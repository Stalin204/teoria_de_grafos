import tkinter as tk
from PIL import Image, ImageTk

# def ventanaRegular(ventana):

#     #Funcion para mostrar que es un grafo
#     ventana=tk.Tk()
#     ventana.title("Grafo Regular")
#     ventana.geometry("500x500")
#     texto = "Un grafo Regular es aquel que todos los grados de sus nodos o vertices son iguales"
    
#     # Crear el Label con el texto ajustado al tamaño de la ventana
#     label = tk.Label(ventana, text=texto)  # El wraplength define el ancho máximo antes de saltar de línea
#     label.pack()
    
#     #image_path = os.path.join(os.path.dirname(__file__), 'images', 'grafosRegulares-removebg-preview(1).png')
#     img = tk.PhotoImage(file="images/grafosRegulares-removebg-preview(1).png")
#     #images\grafosRegulares-removebg-preview(1).png

#    # labelimg = tk.Label(ventana, image=img)  # El wraplength define el ancho máximo antes de saltar de línea
#     #labelimg.pack()

#     # Carga la imagen
#     img_path = "images/grafosRegulares-removebg-preview(1).png"
#     img_pil = Image.open(img_path)
#     img_tk = tk.PhotoImage(file=img_path)

#     # Crea una etiqueta para mostrar la imagen
#     labelimg = tk.Label(ventana,image=tk.PhotoImage(file=img_path))
#     #labelimg.config(image=img_tk)
#     labelimg.pack()

#       # Mantén una referencia a la imagen en memoria
    

#     #ventana.after(10000, ventana.destroy)
#     ventana.mainloop()

#     return ventana



def ventanaRegular(ventana):
    
    ventana = tk.Tk()
    ventana.title("Grafo Regular")
    ventana.geometry("500x500")
    texto = "Un grafo Regular es aquel en el que todos los grados de sus nodos o vértices son iguales"

    label = tk.Label(ventana, text=texto)
    label.pack()

    img_path = "images/grafosRegulares-removebg-preview(1).png"
    img_pil = Image.open(img_path)
    img_tk = ImageTk.PhotoImage(img_pil)
 
    canvas = tk.Canvas(ventana, width=img_pil.width, height=img_pil.height)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.pack()

    # labelimg = tk.Label(ventana)
    # labelimg.configure(image=img_tk)
    # labelimg.image = img_tk  # Mantén una referencia a la imagen en memoria
    # labelimg.pack()

    ventana.mainloop()

    return ventana

#ventanaRegular()