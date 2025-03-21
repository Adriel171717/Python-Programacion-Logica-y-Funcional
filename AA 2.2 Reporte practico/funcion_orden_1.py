# Función que calcula el promedio de un estudiante
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Usando la función
notas = [90, 85, 78, 92]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")
