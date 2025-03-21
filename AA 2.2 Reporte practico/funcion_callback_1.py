# Función principal que recibe un callback
def procesar_datos(datos, callback):
    print(f"Procesando datos: {datos}")
    # Ejecutar el callback al finalizar
    callback()

def notificar_finalizacion():
    print("Proceso finalizado.")

# Llamar a la función con un callback
procesar_datos([1, 2, 3], notificar_finalizacion)
