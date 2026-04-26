import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def abrir_shell(root):
    ventana = tk.Toplevel(root)
    ventana.title("Shell Educativa")
    ventana.geometry("500x350")

    tk.Label(ventana, text="Ingrese un comando (ls/dir, pwd, echo):").pack()

    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=5)

    salida = tk.Text(ventana, height=15, width=60)
    salida.pack()

    def ejecutar():
        comando = entrada.get().strip()
        salida.delete(1.0, tk.END)

        if comando == "":
            messagebox.showwarning("Aviso", "Ingrese un comando")
            return

        try:
            # Adaptar comandos según sistema operativo
            if comando == "ls" and os.name == "nt":
                comando = "dir"
            elif comando == "pwd" and os.name == "nt":
                comando = "cd"

            # Ejecutar comando
            resultado = subprocess.getoutput(comando)

            # Mostrar salida completa
            salida.insert(tk.END, resultado)

        except Exception as e:
            salida.insert(tk.END, f"Error: {str(e)}")

    tk.Button(ventana, text="Ejecutar", command=ejecutar).pack(pady=5)