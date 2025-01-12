import tkinter as tk
from tkinter import messagebox
import os
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.optimize import linprog

class PlanificacionRutas:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Gestion de Ganancias y Recursos")
        self.window.geometry("800x600")

        # Crear carpeta de datos si no existe
        if not os.path.exists('datos'):
            os.makedirs('datos')

        # Archivo de registros
        self.registro_file = 'datos/registro_optimizado.json'
        if not os.path.exists(self.registro_file):
            with open(self.registro_file, 'w') as f:
                json.dump([], f)  # Inicializar con una lista vacía

        # Botón para volver al menú principal
        self.back_button = tk.Button(self.window, text="Volver", command=self.volver)
        self.back_button.place(x=10, y=10)

        # Botón para ver registros
        self.registros_button = tk.Button(self.window, text="Ver Registros", command=self.ver_registros)
        self.registros_button.place(x=70, y=10)

        # Sección de entrada de toneladas disponibles
        self.toneladas_label = tk.Label(self.window, text="Toneladas disponibles de mineral:")
        self.toneladas_label.place(x=10, y=50)

        self.toneladas_a_label = tk.Label(self.window, text="Mineral Oro")
        self.toneladas_a_label.place(x=10, y=80)
        self.toneladas_a = tk.Entry(self.window)
        self.toneladas_a.place(x=120, y=80)

        self.toneladas_b_label = tk.Label(self.window, text="Mineral Plata")
        self.toneladas_b_label.place(x=10, y=110)
        self.toneladas_b = tk.Entry(self.window)
        self.toneladas_b.place(x=120, y=110)

        self.toneladas_c_label = tk.Label(self.window, text="Mineral Cobre")
        self.toneladas_c_label.place(x=10, y=140)
        self.toneladas_c = tk.Entry(self.window)
        self.toneladas_c.place(x=120, y=140)

        # Sección de distribución de paquetes
        self.paquetes_label = tk.Label(self.window, text="Distribución de paquetes de minerales:")
        self.paquetes_label.place(x=10, y=180)

        self.paquete1_label = tk.Label(self.window, text="Paquete 1 contiene:")
        self.paquete1_label.place(x=10, y=210)

        self.paquete1_a_label = tk.Label(self.window, text="Mineral Oro")
        self.paquete1_a_label.place(x=10, y=240)
        self.paquete1_a = tk.Entry(self.window)
        self.paquete1_a.place(x=120, y=240)

        self.paquete1_b_label = tk.Label(self.window, text="Mineral Plata")
        self.paquete1_b_label.place(x=10, y=270)
        self.paquete1_b = tk.Entry(self.window)
        self.paquete1_b.place(x=120, y=270)

        self.paquete1_c_label = tk.Label(self.window, text="Mineral Cobre")
        self.paquete1_c_label.place(x=10, y=300)
        self.paquete1_c = tk.Entry(self.window)
        self.paquete1_c.place(x=120, y=300)

        self.paquete2_label = tk.Label(self.window, text="Paquete 2 contiene:")
        self.paquete2_label.place(x=10, y=330)

        self.paquete2_a_label = tk.Label(self.window, text="Mineral Oro")
        self.paquete2_a_label.place(x=10, y=360)
        self.paquete2_a = tk.Entry(self.window)
        self.paquete2_a.place(x=120, y=360)

        self.paquete2_b_label = tk.Label(self.window, text="Mineral Plata")
        self.paquete2_b_label.place(x=10, y=390)
        self.paquete2_b = tk.Entry(self.window)
        self.paquete2_b.place(x=120, y=390)

        self.paquete2_c_label = tk.Label(self.window, text="Mineral Cobre")
        self.paquete2_c_label.place(x=10, y=420)
        self.paquete2_c = tk.Entry(self.window)
        self.paquete2_c.place(x=120, y=420)

        # Sección de costos de transporte
        self.costos_label = tk.Label(self.window, text="Costo de transporte por bloque:")
        self.costos_label.place(x=10, y=460)

        self.costo_bloque1_label = tk.Label(self.window, text="Bloque 1")
        self.costo_bloque1_label.place(x=10, y=490)
        self.costo_bloque1 = tk.Entry(self.window)
        self.costo_bloque1.place(x=120, y=490)

        self.costo_bloque2_label = tk.Label(self.window, text="Bloque 2")
        self.costo_bloque2_label.place(x=10, y=520)
        self.costo_bloque2 = tk.Entry(self.window)
        self.costo_bloque2.place(x=120, y=520)

        # Botón para calcular la maximización de ganancias
        self.calcular_button = tk.Button(self.window, text="Calcular", command=self.calcular_max_ganancia)
        self.calcular_button.place(x=10, y=550)

        # Área para mostrar la gráfica
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().place(x=300, y=50, width=480, height=450)

        # Etiquetas para mostrar resultados debajo del gráfico
        self.resultado_label = tk.Label(self.window, text="", justify=tk.LEFT)
        self.resultado_label.place(x=300, y=510)

    def volver(self):
        self.window.destroy()
        self.master.deiconify()

    def calcular_max_ganancia(self):
        # Obtener datos de entrada
        toneladas_a = float(self.toneladas_a.get())
        toneladas_b = float(self.toneladas_b.get())
        toneladas_c = float(self.toneladas_c.get())

        paquete1_a = float(self.paquete1_a.get())
        paquete1_b = float(self.paquete1_b.get())
        paquete1_c = float(self.paquete1_c.get())

        paquete2_a = float(self.paquete2_a.get())
        paquete2_b = float(self.paquete2_b.get())
        paquete2_c = float(self.paquete2_c.get())

        costo_bloque1 = float(self.costo_bloque1.get())
        costo_bloque2 = float(self.costo_bloque2.get())

        # Coeficientes de la función objetivo (negativos porque linprog minimiza)
        c = [-costo_bloque1, -costo_bloque2]

        # Restricciones de disponibilidad de minerales
        A = [
            [paquete1_a, paquete2_a],
            [paquete1_b, paquete2_b],
            [paquete1_c, paquete2_c]
        ]
        b = [toneladas_a, toneladas_b, toneladas_c]

        # Resolver el problema de programación lineal
        result = linprog(c, A_ub=A, b_ub=b, method='highs')

        if result.success:
            x1, x2 = result.x
            ganancia_max = -result.fun

            # Mostrar resultados en la etiqueta
            self.resultado_label.config(text=f"Bloques a enviar:\nTipo 1: {x1:.2f}\nTipo 2: {x2:.2f}\nGanancia máxima: {ganancia_max:.2f}$")

            # Graficar las restricciones y la solución
            self.ax.clear()
            x = list(range(0, int(max(toneladas_a, toneladas_b, toneladas_c)) + 1))

            # Graficar cada restricción
            for i, (a, b_val) in enumerate(zip(A, b)):
                if a[1] != 0:  # Evitar división por cero
                    y = [(b_val - a[0] * xi) / a[1] for xi in x]
                    self.ax.plot(x, y, label=f'Mineral {chr(65 + i)}')

            # Marcar la solución óptima
            self.ax.scatter(x1, x2, color='red', label='Solución óptima')
            self.ax.set_xlim(0, max(x))
            self.ax.set_ylim(0, max(x))
            self.ax.set_xlabel('Bloques tipo 1')
            self.ax.set_ylabel('Bloques tipo 2')
            self.ax.legend()
            self.ax.grid(True)
            self.canvas.draw()

            # Guardar el registro
            self.guardar_registro(x1, x2, ganancia_max, A, b)

        else:
            self.resultado_label.config(text="No se pudo encontrar una solución óptima.")

    def guardar_registro(self, x1, x2, ganancia_max, A, b):
        # Crear un diccionario con los datos del registro
        registro = {
            'bloques_tipo_1': x1,
            'bloques_tipo_2': x2,
            'ganancia_max': ganancia_max,
            'restricciones': A,
            'disponibilidad': b,
            'paquete1': {'Oro': A[0][0], 'Plata': A[1][0], 'Cobre': A[2][0]},
            'paquete2': {'Oro': A[0][1], 'Plata': A[1][1], 'Cobre': A[2][1]}
        }

        # Cargar registros existentes
        with open(self.registro_file, 'r') as f:
            registros = json.load(f)

        # Añadir nuevo registro
        registros.append(registro)

        # Guardar registros actualizados
        with open(self.registro_file, 'w') as f:
            json.dump(registros, f)

    def ver_registros(self):
        # Cargar registros
        with open(self.registro_file, 'r') as f:
            registros = json.load(f)

        if not registros:
            messagebox.showwarning("Advertencia", "No hay registros disponibles.")
            return

        # Crear una nueva ventana para mostrar los registros
        registros_window = tk.Toplevel(self.master)
        registros_window.title("Registros")
        registros_window.geometry("680x650")

        # Frame para contener los registros
        registros_frame = tk.Frame(registros_window)
        registros_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas para permitir el scroll
        canvas = tk.Canvas(registros_frame)
        scrollbar = tk.Scrollbar(registros_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Mostrar cada registro
        for i, registro in enumerate(registros):
            # Mostrar la información del registro
            registro_frame = tk.Frame(scrollable_frame, borderwidth=1, relief="solid")
            registro_frame.pack(pady=5, padx=10, fill="x")

            nombre_registro = f"Registro {i + 1}"
            nombre_label = tk.Label(registro_frame, text=nombre_registro, font=("Arial", 12, "bold"))
            nombre_label.pack(side="top", pady=5)

            info_label = tk.Label(registro_frame, text=f"Bloques tipo 1: {registro['bloques_tipo_1']:.2f}, "
                                                       f"Bloques tipo 2: {registro['bloques_tipo_2']:.2f}, "
                                                       f"Ganancia máxima: {registro['ganancia_max']:.2f}$\n"
                                                       f"Paquete 1: Oro: {registro['paquete1']['Oro']} unidades, "
                                                       f"Plata: {registro['paquete1']['Plata']} unidades, "
                                                       f"Cobre: {registro['paquete1']['Cobre']} unidades\n"
                                                       f"Paquete 2: Oro: {registro['paquete2']['Oro']} unidades, "
                                                       f"Plata: {registro['paquete2']['Plata']} unidades, "
                                                       f"Cobre: {registro['paquete2']['Cobre']} unidades")
            info_label.pack(side="top")

            # Mostrar la gráfica directamente
            self.mostrar_grafica(registro, registro_frame)

            # Botón para borrar el registro
            borrar_button = tk.Button(registro_frame, text="Borrar", command=lambda i=i: self.borrar_registro(i, registros_window))
            borrar_button.pack(side="bottom")

        # Botón para borrar todos los registros
        borrar_todos_button = tk.Button(registros_window, text="Borrar Todos", command=lambda: self.borrar_todos_registros(registros_window))
        borrar_todos_button.pack(pady=10)

    def mostrar_grafica(self, registro, parent_frame):
        # Crear una figura y un eje para la gráfica
        fig, ax = plt.subplots()

        # Graficar las restricciones y la solución
        x = list(range(0, int(max(registro['disponibilidad'])) + 1))

        # Graficar cada restricción
        for i, (a, b_val) in enumerate(zip(registro['restricciones'], registro['disponibilidad'])):
            if a[1] != 0:  # Evitar división por cero
                y = [(b_val - a[0] * xi) / a[1] for xi in x]
                ax.plot(x, y, label=f'Mineral {chr(65 + i)}')

        # Marcar la solución óptima
        ax.scatter(registro['bloques_tipo_1'], registro['bloques_tipo_2'], color='red', label='Solución óptima')
        ax.set_xlim(0, max(x))
        ax.set_ylim(0, max(x))
        ax.set_xlabel('Bloques tipo 1')
        ax.set_ylabel('Bloques tipo 2')
        ax.legend()
        ax.grid(True)

        # Mostrar la gráfica en el frame del registro
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

    def borrar_registro(self, index, window):
        # Cargar registros
        with open(self.registro_file, 'r') as f:
            registros = json.load(f)

        # Eliminar el registro seleccionado
        if 0 <= index < len(registros):
            del registros[index]

            # Guardar registros actualizados
            with open(self.registro_file, 'w') as f:
                json.dump(registros, f)

            # Actualizar la ventana
            window.destroy()
            self.ver_registros()

    def borrar_todos_registros(self, window):
        # Confirmar la acción
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas borrar todos los registros?"):
            # Vaciar el archivo de registros
            with open(self.registro_file, 'w') as f:
                json.dump([], f)

            # Cerrar la ventana de registros
            window.destroy()