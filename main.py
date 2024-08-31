# main.py
import tkinter as tk
from model import TaskModel
from view import TaskView
from controller import TaskController

if __name__ == "__main__":
    root = tk.Tk()

    # Crear modelo, vista y controlador
    model = TaskModel()
    view = TaskView(root)
    controller = TaskController(model, view)

    # Iniciar el loop de la aplicación
    root.mainloop()
