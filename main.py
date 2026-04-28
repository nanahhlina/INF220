# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.view import CalculadoraView
from controllers.controller import CalculadoraController
from models.model import Fraccion

def main():
    root = tk.Tk()
    root.title("Calculadora de Fracciones")

    model = Fraccion()
    view = CalculadoraView(root)
    controller = CalculadoraController(view, model)

    root.mainloop()

if __name__ == "__main__":
    main()