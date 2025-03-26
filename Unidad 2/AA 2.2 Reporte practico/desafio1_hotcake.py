def preparar_hotcake():
    return '🥞'

def ordenar_hotcake(num_piezas):
    piezas_hotcakes = [preparar_hotcake() for _ in range(num_piezas)]

    return piezas_hotcakes

mi_familia = ordenar_hotcake(int(input('Cuantos son en tu familia?: ')))

print(mi_familia)