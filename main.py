import tkinter as tk
from control import ControlAutomatizado
from rutas_eficientes import RutasEficientes
from planificacion_rutas import PlanificacionRutas  # Importa la nueva clase

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Control de Extracción de Minerales")
        self.master.geometry("300x300")

        self.label = tk.Label(master, text="Menú Principal", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button_control = tk.Button(master, text="Control Automatizado", command=self.open_control)
        self.button_control.pack(pady=10)

        self.button_rutas = tk.Button(master, text="Rutas Más Eficientes", command=self.open_rutas)
        self.button_rutas.pack(pady=10)

        self.button_planificacion = tk.Button(master, text="Maximizar Ganancias", command=self.open_planificacion)
        self.button_planificacion.pack(pady=10)

        self.button_salir = tk.Button(master, text="Salir", command=master.quit)
        self.button_salir.pack(pady=10)

    def open_control(self):
        self.master.withdraw()  # Oculta la ventana principal
        self.control_window = ControlAutomatizado(self.master)

    def open_rutas(self):
        self.master.withdraw()  # Oculta la ventana principal
        self.rutas_window = RutasEficientes(self.master)

    def open_planificacion(self):
        self.master.withdraw()  # Oculta la ventana principal
        self.planificacion_window = PlanificacionRutas(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()