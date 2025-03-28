def cuadradosLista(arreglo):
    
    enteros_positivos = filter(lambda x: x > 0 and x == int(x), arreglo)
    
    cuadrados = map(lambda x: x ** 2, enteros_positivos)
    
    return list(cuadrados)


cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)