import os
import platform
import shutil
import tkinter as tk

def abrir_info(root):
    ventana = tk.Toplevel(root)
    ventana.title("Información del Sistema")
    ventana.geometry("400x200")

    try:
        usuario = os.getlogin()
    except:
        usuario = "Usuario"

    sistema = platform.system() + " " + platform.release()
    disco = shutil.disk_usage("/")

    texto = f"""
Usuario: {usuario}
Sistema: {sistema}
Espacio libre: {disco.free // (1024**3)} GB
"""

    tk.Label(ventana, text=texto).pack()