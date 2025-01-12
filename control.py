import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np  # Importar numpy para resolver sistemas de ecuaciones


class ControlAutomatizado(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Control Automatizado")
        self.geometry("900x850")

        # Crear un marco para dividir la pantalla
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Sección izquierda para ingreso de datos
        self.frame_izquierda = tk.Frame(self.frame_principal)
        self.frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 5), pady=10)

        # Sección derecha para gráficos y registros
        self.frame_derecha = tk.Frame(self.frame_principal)
        self.frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 10), pady=10)

        # Frame para los botones de la parte superior izquierda
        self.frame_botones_superior = tk.Frame(self.frame_izquierda)
        self.frame_botones_superior.pack(anchor='nw')

        # Botón para volver al menú principal
        btn_volver = tk.Button(self.frame_botones_superior, text="Volver al Menú Principal", command=self.volver_a_menu)
        btn_volver.pack(side=tk.LEFT)

        # Botón para ver registros anteriores
        btn_ver_registros = tk.Button(self.frame_botones_superior, text="Ver Registros Anteriores", command=self.ver_registros)
        btn_ver_registros.pack(side=tk.LEFT, padx=(10, 0))  # Espaciado a la izquierda

        # Título de la sección
        tk.Label(self.frame_izquierda, text="Datos de Extracción", font=("Arial", 16)).pack(pady=(20, 10))

        # Entradas de los datos de extracción
        self.create_input_fields()

        # Botón para calcular
        btn_calcular = tk.Button(self.frame_izquierda, text="Calcular", command=self.calcular_control_automatizado)
        btn_calcular.pack(pady=20)

        # Label para mostrar los resultados
        self.label_resultado = tk.Label(self.frame_izquierda, text="")
        self.label_resultado.pack()

        # Inicializamos la figura para la gráfica
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame_derecha)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Label de gráficos
        self.label_graficos = tk.Label(self.frame_derecha, text="Gráficos de Resultados", font=("Arial", 16))
        self.label_graficos.pack(pady=10)

    def create_input_fields(self):
        """Crea los campos de entrada para los datos de extracción y límite de tiempo."""
        # Equipo 1
        tk.Label(self.frame_izquierda, text="Equipo 1 extrae:").pack(anchor='w', padx=20)
        tk.Label(self.frame_izquierda, text="Mineral (Oro):").pack(anchor='w', padx=20)
        self.entry_equipo1_a = tk.Entry(self.frame_izquierda)
        self.entry_equipo1_a.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plata):").pack(anchor='w', padx=20)
        self.entry_equipo1_b = tk.Entry(self.frame_izquierda)
        self.entry_equipo1_b.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plomo):").pack(anchor='w', padx=20)
        self.entry_equipo1_c = tk.Entry(self.frame_izquierda)
        self.entry_equipo1_c.pack(padx=20)

        # Equipo 2
        tk.Label(self.frame_izquierda, text="Equipo 2 extrae:").pack(anchor='w', padx=20)
        tk.Label(self.frame_izquierda, text="Mineral (Oro):").pack(anchor='w', padx=20)
        self.entry_equipo2_a = tk.Entry(self.frame_izquierda)
        self.entry_equipo2_a.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plata):").pack(anchor='w', padx=20)
        self.entry_equipo2_b = tk.Entry(self.frame_izquierda)
        self.entry_equipo2_b.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plomo):").pack(anchor='w', padx=20)
        self.entry_equipo2_c = tk.Entry(self.frame_izquierda)
        self.entry_equipo2_c.pack(padx=20)

        # Equipo 3
        tk.Label(self.frame_izquierda, text="Equipo 3 extrae:").pack(anchor='w', padx=20)
        tk.Label(self.frame_izquierda, text="Mineral (Oro):").pack(anchor='w', padx=20)
        self.entry_equipo3_a = tk.Entry(self.frame_izquierda)
        self.entry_equipo3_a.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plata):").pack(anchor='w', padx=20)
        self.entry_equipo3_b = tk.Entry(self.frame_izquierda)
        self.entry_equipo3_b.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plomo):").pack(anchor='w', padx=20)
        self.entry_equipo3_c = tk.Entry(self.frame_izquierda)
        self.entry_equipo3_c.pack(padx=20)

        # Datos Totales
        tk.Label(self.frame_izquierda, text="Total de minerales deseados:").pack(anchor='w', padx=20)
        tk.Label(self.frame_izquierda, text="Mineral (Oro):").pack(anchor='w', padx=20)
        self.entry_total_a = tk.Entry(self.frame_izquierda)
        self.entry_total_a.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plata):").pack(anchor='w', padx=20)
        self.entry_total_b = tk.Entry(self.frame_izquierda)
        self.entry_total_b.pack(padx=20)

        tk.Label(self.frame_izquierda, text="Mineral (Plomo):").pack(anchor='w', padx=20)
        self.entry_total_c = tk.Entry(self.frame_izquierda)
        self.entry_total_c.pack(padx=20)

        # Límite de tiempo
        tk.Label(self.frame_izquierda, text="Límite de Tiempo (horas):").pack(anchor='w', padx=20)
        self.entry_limite_tiempo = tk.Entry(self.frame_izquierda)
        self.entry_limite_tiempo.pack(padx=20)

    def calcular_control_automatizado(self):
        """Realiza los cálculos de control automatizado usando sistemas de ecuaciones lineales."""
        try:
            equipo1_a = int(self.entry_equipo1_a.get())
            equipo1_b = int(self.entry_equipo1_b.get())
            equipo1_c = int(self.entry_equipo1_c.get())

            equipo2_a = int(self.entry_equipo2_a.get())
            equipo2_b = int(self.entry_equipo2_b.get())
            equipo2_c = int(self.entry_equipo2_c.get())

            equipo3_a = int(self.entry_equipo3_a.get())
            equipo3_b = int(self.entry_equipo3_b.get())
            equipo3_c = int(self.entry_equipo3_c.get())

            total_a = int(self.entry_total_a.get())
            total_b = int(self.entry_total_b.get())
            total_c = int(self.entry_total_c.get())

            limite_tiempo = int(self.entry_limite_tiempo.get())

            # Definir el sistema de ecuaciones
            A = np.array([[equipo1_a, equipo2_a, equipo3_a],
                          [equipo1_b, equipo2_b, equipo3_b],
                          [equipo1_c, equipo2_c, equipo3_c]])
            B = np.array([total_a, total_b, total_c])

            # Resolver el sistema de ecuaciones
            horas_necesarias = np.linalg.solve(A, B)

            # Construir el resultado con mensajes adicionales
            resultado_texto = "Horas necesarias para cada equipo:\n"
            for i, horas in enumerate(horas_necesarias):
                if horas < 0:
                    resultado_texto += f"Equipo {i + 1}: {horas:.2f} horas (riesgo)\n"
                elif horas > limite_tiempo:
                    resultado_texto += f"Equipo {i + 1}: {horas:.2f} horas (se excede)\n"
                else:
                    resultado_texto += f"Equipo {i + 1}: {horas:.2f} horas\n"

            resultado_texto += f"Límite de tiempo establecido: {limite_tiempo} horas"
            self.label_resultado.config(text=resultado_texto)

            # Guardar resultados en el registro
            self.save_results(horas_necesarias, limite_tiempo)
            self.update_graph(horas_necesarias, limite_tiempo)  # Actualizar la gráfica

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "El sistema de ecuaciones no tiene solución única.")

    def save_results(self, horas_necesarias, limite_tiempo):
        """Guarda los resultados en un archivo JSON, incluyendo el color de las barras."""
        try:
            with open("datos/registros.json", "r") as f:
                registros = json.load(f)
        except FileNotFoundError:
            registros = []

        # Determinar colores
        colors = []
        for x in horas_necesarias:
            if x < 0 or x > limite_tiempo:
                colors.append('rojo')  # Excede el límite o negativo
            elif x >= limite_tiempo - 1:  # Proximidad al límite
                colors.append('amarillo')
            else:
                colors.append('verde')

        registros.append({
            "equipo_1_horas": horas_necesarias[0],
            "equipo_2_horas": horas_necesarias[1],
            "equipo_3_horas": horas_necesarias[2],
            "limite_tiempo": limite_tiempo,
            "colores": colors  # Guardar los colores
        })

        with open("datos/registros.json", "w") as f:
            json.dump(registros, f, indent=4)

    def update_graph(self, horas_necesarias, limite_tiempo):
        """Actualiza la gráfica con los nuevos resultados y colores según el tiempo."""
        self.ax.clear()  # Limpiar los ejes antes de dibujar
        labels = ['Equipo 1', 'Equipo 2', 'Equipo 3']

        # Determinar colores para las barras
        colors = []
        for x in horas_necesarias:
            if x < 0 or x > limite_tiempo:
                colors.append('red')  # Excede el límite o negativo
            elif x >= limite_tiempo - 1:  # Proximidad al límite
                colors.append('yellow')
            else:
                colors.append('green')

        self.ax.bar(labels, horas_necesarias, color=colors)
        self.ax.set_ylabel('Horas de operación')
        self.ax.set_title('Horas necesarias para cada equipo')
        self.canvas.draw()  # Redibujar en el canvas

    def ver_registros(self):
        """Muestra los registros anteriores en una nueva ventana."""
        try:
            with open("datos/registros.json", "r") as f:
                registros = json.load(f)

            RegistroVentana(self, registros)
        except FileNotFoundError:
            messagebox.showinfo("Registros Anteriores", "No hay registros disponibles.")

    def volver_a_menu(self):
        """Cierra la ventana actual y muestra el menú principal."""
        self.destroy()  # Cierra la ventana de Control Automatizado
        self.master.deiconify()  # Muestra la ventana principal nuevamente


class RegistroVentana(tk.Toplevel):
    def __init__(self, master, registros):
        super().__init__(master)
        self.title("Registros Anteriores")
        self.geometry("650x600")

        self.registros = registros

        # Frame para el scroll
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Botón para eliminar todos los registros (en la parte superior)
        btn_eliminar_todos = tk.Button(self, text="Eliminar Todos", command=self.eliminar_todos)
        btn_eliminar_todos.pack(pady=10)

        # Crear registros
        self.create_registros()

    def create_registros(self):
        """Crea una interfaz para mostrar cada registro."""
        for i, registro in enumerate(self.registros):
            frame_registro = tk.Frame(self.scrollable_frame)
            frame_registro.pack(pady=5)

            # Mostrar texto del registro
            tk.Label(frame_registro, text=f"Registro {i + 1}:\n"
                                          f"Equipo 1: {registro['equipo_1_horas']:.2f} horas\n"
                                          f"Equipo 2: {registro['equipo_2_horas']:.2f} horas\n"
                                          f"Equipo 3: {registro['equipo_3_horas']:.2f} horas\n"
                                          f"Límite de tiempo: {registro['limite_tiempo']} horas").pack()

            # Crear gráfica para cada registro con los colores correspondientes
            fig, ax = plt.subplots()
            colors = ['red' if color == 'rojo' else 'yellow' if color == 'amarillo' else 'green' for color in
                      registro['colores']]
            ax.bar(['Equipo 1', 'Equipo 2', 'Equipo 3'],
                   [registro['equipo_1_horas'], registro['equipo_2_horas'], registro['equipo_3_horas']],
                   color=colors)
            ax.set_ylabel('Horas de operación')
            ax.set_title('Horas de extracción para cada equipo')

            fig.tight_layout()  # Ajustar el layout para que no se corte
            canvas = FigureCanvasTkAgg(fig, master=frame_registro)
            canvas.get_tk_widget().pack()

            # Botón para eliminar el registro actual
            btn_eliminar = tk.Button(frame_registro, text="Eliminar", command=lambda idx=i: self.eliminar_registro(idx))
            btn_eliminar.pack(pady=5)

    def eliminar_registro(self, idx):
        """Elimina un registro específico."""
        self.registros.pop(idx)
        self.update_registros_file()
        self.destroy()  # Cierra la ventana actual
        RegistroVentana(self.master, self.registros)  # Vuelve a abrir la ventana actualizada

    def eliminar_todos(self):
        """Elimina todos los registros."""
        self.registros.clear()
        self.update_registros_file()
        self.destroy()  # Cierra la ventana actual
        messagebox.showinfo("Información", "Todos los registros han sido eliminados.")

    def update_registros_file(self):
        """Actualiza el archivo de registros."""
        with open("datos/registros.json", "w") as f:
            json.dump(self.registros, f, indent=4)
