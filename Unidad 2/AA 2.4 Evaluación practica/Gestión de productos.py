
productos = ["Frijoles Refritos", "Coca Cola", "Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]

# 1. Ordenar alfabéticamente
productos_ordenados = sorted(productos)

# 2. Convertir a cadena de nombres ordenados
cadena_ordenada = ", ".join(productos_ordenados)

# 3. Convertir cada nombre a slug
slugs = list(map(lambda x: x.lower().replace(" ", "-"), productos_ordenados))

# Imprimir
print("a. Lista de slugs:")
print(slugs)
print("\nb. Cadena de nombres en orden alfabético:")
print(cadena_ordenada)