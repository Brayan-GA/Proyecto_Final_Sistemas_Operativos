import tkinter as tk
from modulos.explorador import abrir_explorador
from modulos.procesos import abrir_procesos
from modulos.shell import abrir_shell
from modulos.sistema import abrir_info

root = tk.Tk()
root.title("Mini Sistema Operativo")
root.geometry("400x300")

tk.Button(root, text="Explorador de Archivos", command=lambda: abrir_explorador(root)).pack(pady=5)
tk.Button(root, text="Gestión de Procesos", command=lambda: abrir_procesos(root)).pack(pady=5)
tk.Button(root, text="Shell Educativa", command=lambda: abrir_shell(root)).pack(pady=5)
tk.Button(root, text="Información del Sistema", command=lambda: abrir_info(root)).pack(pady=5)

root.mainloop()