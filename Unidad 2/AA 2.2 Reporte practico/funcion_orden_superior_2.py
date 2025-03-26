# Usar filter para filtrar los números pares de una lista
def es_par(num):
    return num % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(es_par, numeros))
print(f"Números pares: {pares}")
