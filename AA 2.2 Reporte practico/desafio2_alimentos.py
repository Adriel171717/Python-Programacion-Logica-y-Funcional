def pizza():
    return '🍕'

def hambuguesa():
    return '🍔'

def hotdog():
    return '🌭'

def bonus(num_porciones):
    if num_porciones > 2:
        return '🥤 coca gratis'
    else:
        return ''

def ordenar_alimento(funcion, num_porciones):
    porciones = [funcion() for _ in range(num_porciones)]
    
    alimentos = bonus(num_porciones)

    return porciones, alimentos


# Ordenar alimentos
GrupoPizza = ordenar_alimento(pizza, 5)
GrupoHamburguesa = ordenar_alimento(hambuguesa, 7)
GrupoHotdog = ordenar_alimento(hotdog, 4)

# Imprimir las porciones ordenadas
print('Grupo Pizza:', GrupoPizza)
print('Grupo Hamburguesa:', GrupoHamburguesa)
print('Grupo Hotdog:', GrupoHotdog)