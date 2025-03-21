# Usar map para aplicar una función a una lista
def al_cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
resultado = list(map(al_cuadrado, numeros))
print(f"Números al cuadrado: {resultado}")
