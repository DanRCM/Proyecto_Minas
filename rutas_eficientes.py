import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools

class RutasEficientes:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Rutas Más Eficientes")
        self.window.geometry("1000x600")

        # Crear frames para organizar la interfaz
        self.left_frame = tk.Frame(self.window)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.right_frame = tk.Frame(self.window)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botón para volver al menú principal
        self.back_button = tk.Button(self.left_frame, text="Volver al Menú Principal", command=self.back_to_main)
        self.back_button.pack(pady=5)

        # Controles en el lado izquierdo
        self.label = tk.Label(self.left_frame, text="Calcular Rutas y Costos", font=("Arial", 14))
        self.label.pack(pady=10)

        self.locations = ["Mina A", "Almacén B", "Puerto C", "Fábrica D", "Depósito E"]
        self.cost_matrix = np.array([
            [0, 10, 15, 20, 25],
            [10, 0, 5, 10, 15],
            [15, 5, 0, 5, 10],
            [20, 10, 5, 0, 5],
            [25, 15, 10, 5, 0]
        ])

        self.start_label = tk.Label(self.left_frame, text="Ubicación de inicio:")
        self.start_label.pack(pady=5)
        self.start_var = tk.StringVar()
        self.start_menu = tk.OptionMenu(self.left_frame, self.start_var, *self.locations)
        self.start_menu.pack(pady=5)

        self.end_label = tk.Label(self.left_frame, text="Ubicación de destino:")
        self.end_label.pack(pady=5)
        self.end_var = tk.StringVar()
        self.end_menu = tk.OptionMenu(self.left_frame, self.end_var, *self.locations)
        self.end_menu.pack(pady=5)

        self.calculate_button = tk.Button(self.left_frame, text="Calcular Rutas", command=self.calculate_routes)
        self.calculate_button.pack(pady=20)

        self.matrix_label = tk.Label(self.left_frame, text=self.format_matrix(), font=("Arial", 10))
        self.matrix_label.pack(pady=5)

        # Gráfico y resultados en el lado derecho
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.right_frame)
        self.canvas.get_tk_widget().pack()

        self.routes_info_label = tk.Label(self.right_frame, text="", font=("Arial", 10), justify="left")
        self.routes_info_label.pack(pady=10)

    def format_matrix(self):
        matrix_str = "Matriz de Costos:\n"
        for row in self.cost_matrix:
            matrix_str += " ".join(f"{int(cost):2d}" for cost in row) + "\n"
        return matrix_str

    def calculate_routes(self):
        start = self.start_var.get()
        end = self.end_var.get()

        if start == end:
            self.ax.clear()
            self.ax.text(0.5, 0.5, "La ubicación de inicio y destino son las mismas.", ha='center', va='center', fontsize=12)
            self.canvas.draw()
            self.routes_info_label.config(text="")
            return

        start_index = self.locations.index(start)
        end_index = self.locations.index(end)

        # Generar todas las rutas posibles entre las ubicaciones
        all_routes = list(itertools.permutations(range(len(self.locations))))
        valid_routes = [route for route in all_routes if route[0] == start_index and route[-1] == end_index]

        route_costs = []
        route_labels = []
        routes_info = []

        for idx, route in enumerate(valid_routes):
            cost = 0
            route_str = self.locations[route[0]]
            for i in range(len(route) - 1):
                cost += self.cost_matrix[route[i], route[i + 1]]
                route_str += f" → {self.locations[route[i + 1]]}"
            route_costs.append(cost)
            route_labels.append(f"Ruta {idx + 1}")
            routes_info.append(f"Ruta {idx + 1}: {route_str} - Costo: {cost}")

        self.plot_routes(route_labels, route_costs)
        self.routes_info_label.config(text="\n".join(routes_info))

    def plot_routes(self, route_labels, route_costs):
        self.ax.clear()
        self.ax.bar(route_labels, route_costs, color='skyblue')
        self.ax.set_ylabel('Costo')
        self.ax.set_title('Costos de Rutas Posibles')
        self.canvas.draw()

    def back_to_main(self):
        self.window.destroy()
        self.window.master.deiconify()