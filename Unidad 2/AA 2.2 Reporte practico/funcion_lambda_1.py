# Usar lambda para ordenar una lista de estudiantes por sus promedios
estudiantes = [("Carlos", 85), ("Ana", 92), ("Luis", 78)]
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1])
print(f"Estudiantes ordenados por promedio: {estudiantes_ordenados}")
