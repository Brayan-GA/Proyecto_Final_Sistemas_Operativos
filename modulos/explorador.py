import os
import tkinter as tk

def abrir_explorador(root):
    ventana = tk.Toplevel(root)
    ventana.title("Explorador de Archivos")
    ventana.geometry("400x300")

    path = tk.StringVar()
    path.set(os.getcwd())

    lista = tk.Listbox(ventana, width=50)
    lista.pack()

    def listar():
        lista.delete(0, tk.END)
        archivos = os.listdir(path.get())
        if not archivos:
            lista.insert(tk.END, "Carpeta vacía")
        else:
            for f in archivos:
                lista.insert(tk.END, f)

    def subir():
        path.set(os.path.dirname(path.get()))
        listar()

    tk.Button(ventana, text="Refrescar", command=listar).pack()
    tk.Button(ventana, text="Subir nivel", command=subir).pack()

    listar()