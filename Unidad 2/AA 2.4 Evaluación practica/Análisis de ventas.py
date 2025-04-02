from functools import reduce

tipo_cambio = 20.45
ventas_mxn = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

# 1. Calcular el promedio de ventas en pesos mexicanos
total_ventas = reduce(lambda x, y: x + y, ventas_mxn)
promedio_mxn = total_ventas / len(ventas_mxn)

# 2. Convertir las ventas a dólares
ventas_usd = list(map(lambda x: x / tipo_cambio, ventas_mxn))

# 3. Filtrar las ventas mayores a 150 dolares
ventas_mayores_150 = list(filter(lambda x: x > 150, ventas_usd))

# 4. Calcular la suma total de las ventas filtradas
total_ventas_mayores_150 = reduce(lambda x, y: x + y, ventas_mayores_150, 0)

# Imprimir
print(f"Promedio de ventas en pesos mexicanos: {promedio_mxn:.2f} MXN")
print("Ventas en dólares: " + ", ".join(map(lambda x: f"{x:.2f} USD", ventas_usd)))
print("Ventas en dólares mayores a 150: " + ", ".join(map(lambda x: f"{x:.2f} USD", ventas_mayores_150)))
print(f"Suma total de ventas mayores a 150 dólares: {total_ventas_mayores_150:.2f} USD")
