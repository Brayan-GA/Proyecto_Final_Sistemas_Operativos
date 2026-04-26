import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

def abrir_procesos(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestión de Procesos")
    ventana.geometry("400x300")

    lista = tk.Listbox(ventana, width=50)
    lista.pack()

    def listar():
        lista.delete(0, tk.END)
        resultado = subprocess.getoutput("tasklist" if os.name == "nt" else "ps aux")
        for linea in resultado.split("\n"):
            lista.insert(tk.END, linea)

    def matar():
        pid = simpledialog.askstring("PID", "Ingrese el PID:")
        if pid:
            try:
                os.system(f"taskkill /PID {pid} /F" if os.name == "nt" else f"kill -9 {pid}")
                messagebox.showinfo("Éxito", "Proceso finalizado")
            except:
                messagebox.showerror("Error", "No se pudo finalizar")

    tk.Button(ventana, text="Listar procesos", command=listar).pack()
    tk.Button(ventana, text="Finalizar proceso", command=matar).pack()