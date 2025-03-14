# Objetivo: Control de flujo de un programa
# Ejercicio 3: Programa que simula el lanzamiento de una moneda

import random

num = random.randint(0, 1)
if num == 0:
    print('Cara')
else:
    print('Cruz')

# Ejercicio: Programa que simula la bola mágica

pregunta = input('Pregunta: ')
numero_elatorio = random.randint(1, 9)

if numero_elatorio == 1:
    respuesta = 'Si - definitivamente'
elif numero_elatorio == 2:
    respuesta = 'Esta decidido'
elif numero_elatorio == 3:
    respuesta = 'Sin duda'
elif numero_elatorio == 4:
    respuesta = 'Respuesta confusa, intenta de nuevo'
elif numero_elatorio == 5:
    respuesta = 'Pregunta más tarde'
elif numero_elatorio == 6:
    respuesta = 'Mejor no te digo'
elif numero_elatorio == 7:
    respuesta = 'Mis fuentes dicen queno'
elif numero_elatorio == 8:
    respuesta = 'No parece bueno'
elif numero_elatorio == 9:
    respuesta = 'Muy dudoso'
else:
    respuesta = 'Error'

print('Bola mágica: ' + respuesta)
