# Función que determina si un estudiante aprobó o no basado en su nota
def es_aprobado(nota):
    return nota >= 60

# Usando la función
nota_estudiante = 75
resultado = es_aprobado(nota_estudiante)
print(f"El estudiante {'aprobó' if resultado else 'no aprobó'}.")
