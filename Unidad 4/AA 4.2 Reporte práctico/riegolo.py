# Estado de sensores
def humedad_suelo():
    return 'baja'

def temperatura():
    return 35

def hora():
    return 20

def pronostico_lluvia():
    return False

# ¿Es una hora adecuada para regar?
def hora_adecuada(h):
    return h < 10 or h > 18

# ¿Se debe activar el sistema de riego?
def activar_riego():
    return (
        humedad_suelo() == 'baja'
        and not pronostico_lluvia()
        and hora_adecuada(hora())
    )

# Diagnóstico del sistema
def estado_riego():
    return 'Activado' if activar_riego() else 'No activado'

# Alerta de temperatura extrema
def alerta_calor():
    return temperatura() >= 32

# Mensaje de recomendación si se activa el riego con calor extremo
def recomendacion():
    if activar_riego() and alerta_calor():
        return 'Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.'
    return 'Sin recomendaciones especiales para el riego.'

# Ejecución del sistema
if __name__ == '__main__':
    print(f"Estado del riego: {estado_riego()}")
    print(f"Recomendación: {recomendacion()}")
