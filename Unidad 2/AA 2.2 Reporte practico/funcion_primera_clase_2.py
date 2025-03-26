# Retornar una función desde otra función
def obtener_funcion_despedida():
    def despedida():
        print("¡Adiós, que tengas un buen día!")
    return despedida

# Usar la función retornada
funcion_despedida = obtener_funcion_despedida()
funcion_despedida()
