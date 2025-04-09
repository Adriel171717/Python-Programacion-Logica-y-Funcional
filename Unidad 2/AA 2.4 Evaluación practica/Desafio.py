import tkinter as tk
from functools import reduce
from tkinter import messagebox
import statistics

# Configuración inicial
MATERIAS = ["Programación I", "Bases de Datos", "Inteligencia Artificial"]
ASPECTOS = [
    "Contenido/Temática", 
    "Nivel de Complejidad", 
    "Herramientas utilizadas", 
    "Actividades prácticas"
]
ESCALA = {1: "Insuficiente", 2: "Regular", 3: "Aceptable", 4: "Bueno", 5: "Excelente"}

# ----- Funciones puras para cálculos -----

def calcular_promedio(valores):
    return reduce(lambda a, b: a + b, valores) / len(valores) if valores else 0

def calcular_desviacion(valores):
    return statistics.stdev(valores) if len(valores) > 1 else 0

# Reorganiza datos por comprensión de listas usando lambda
def combinar_aspectos(evaluaciones):
    return list(map(
        lambda i: list(map(lambda e: e["valoraciones"][i], evaluaciones)),
        range(len(ASPECTOS))
    ))

def calcular_metricas_generales(evaluaciones):
    todas_valoraciones = list(map(lambda e: e["valoraciones"], evaluaciones))
    todas_valoraciones_planas = reduce(lambda acc, val: acc + val, todas_valoraciones, [])
    aspectos_combinados = combinar_aspectos(evaluaciones)

    return {
        "promedio_general": calcular_promedio(todas_valoraciones_planas),
        "maximo_general": max(todas_valoraciones_planas) if todas_valoraciones_planas else 0,
        "minimo_general": min(todas_valoraciones_planas) if todas_valoraciones_planas else 0,
        "suma_total": sum(todas_valoraciones_planas),
        "total_evaluaciones": len(evaluaciones),
        "promedios_aspectos": list(map(calcular_promedio, aspectos_combinados)),
        "desviaciones_aspectos": list(map(calcular_desviacion, aspectos_combinados))
    }

# ----- Interfaz gráfica -----

class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluación de Asignaturas")

        # Variables
        self.materia_var = tk.StringVar()
        self.valoraciones_vars = list(map(lambda _: tk.IntVar(value=3), ASPECTOS))
        self.evaluaciones = []
        
        
        # Crear las interfaces
        self.crear_interfaz_ingreso()
        self.crear_interfaz_resultados()

    def crear_interfaz_ingreso(self):
        frame = tk.LabelFrame(self.root, text="Nueva Evaluación", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill="x")

        # Materia
        tk.Label(frame, text="Materia:").grid(row=0, column=0, sticky="w")
        tk.OptionMenu(frame, self.materia_var, *MATERIAS).grid(row=0, column=1, sticky="ew", pady=5)
        
        # Valoraciones
        list(map(lambda i_as: (
            tk.Label(frame, text=f"{i_as[1]} (1-5):").grid(row=i_as[0]+1, column=0, sticky="w"),
            tk.Scale(frame, variable=self.valoraciones_vars[i_as[0]], from_=1, to=5, orient="horizontal")
              .grid(row=i_as[0]+1, column=1, sticky="ew")
        ), enumerate(ASPECTOS)))

        # Botones
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=len(ASPECTOS)+1, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Agregar Evaluación", command=self.agregar_evaluacion).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Calcular Resultados", command=self.mostrar_resultados).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Limpiar Todo", command=self.limpiar_todo).pack(side="left", padx=5)

    def crear_interfaz_resultados(self):
        frame = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Área de resultados
        self.resultados_text = tk.Text(frame, height=15, wrap="word")
        self.resultados_text.pack(fill="both", expand=True)
        
        # Barra de desplazamiento
        scrollbar = tk.Scrollbar(self.resultados_text)
        scrollbar.pack(side="right", fill="y")
        self.resultados_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.resultados_text.yview)

    def agregar_evaluacion(self):
        try:
            materia = self.materia_var.get()
            if not materia:
                raise ValueError("Seleccione una materia")

            valoraciones = list(map(lambda v: v.get(), self.valoraciones_vars))

            self.evaluaciones.append({
                "materia": materia,
                "valoraciones": valoraciones
            })

            messagebox.showinfo("Éxito", "Evaluación agregada correctamente")
            self.limpiar_formulario()

        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {str(e)}")

    # Limpiar datos y regresar lo por defecto "(3)"
    def limpiar_formulario(self):
        self.materia_var.set("")
        list(map(lambda v: v.set(3), self.valoraciones_vars))

    # Eliminar datos Incluyendo los guardados
    def limpiar_todo(self):
        self.evaluaciones.clear()
        self.limpiar_formulario()
        self.resultados_text.config(state="normal")
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.config(state="disabled")
        messagebox.showinfo("Información", "Todos los datos han sido eliminados")

    # Mostrar resultados generales
    def mostrar_resultados(self):
        if not self.evaluaciones:
            messagebox.showinfo("Información", "No hay evaluaciones registradas")
            return

        metricas = calcular_metricas_generales(self.evaluaciones)

        # Mostrar Todos los resultados
        texto = "RESULTADOS GENERALES\n\n"
        texto += f"Total evaluaciones: {metricas['total_evaluaciones']}\n"
        texto += f"Promedio general: {metricas['promedio_general']:.2f} ({ESCALA[round(metricas['promedio_general'])]})\n"
        texto += f"Valoración máxima: {metricas['maximo_general']} ({ESCALA[metricas['maximo_general']]})\n"
        texto += f"Valoración mínima: {metricas['minimo_general']} ({ESCALA[metricas['minimo_general']]})\n"
        texto += f"Suma total: {metricas['suma_total']}\n\n"

        texto += "RESULTADOS POR ASPECTO\n\n"

        texto += ''.join(map(lambda data: (
            f"{data[0]}:\n"
            f"  Promedio: {data[1]:.2f} ({ESCALA[round(data[1])]})\n"
            f"  Desviación estándar: {data[2]:.2f}\n\n"
        ), zip(ASPECTOS, metricas["promedios_aspectos"], metricas["desviaciones_aspectos"])))

        self.resultados_text.config(state="normal")
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.insert(tk.END, texto)
        self.resultados_text.config(state="disabled")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = EncuestaApp(root)
    root.mainloop()
