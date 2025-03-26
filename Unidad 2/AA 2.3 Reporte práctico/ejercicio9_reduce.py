from functools import reduce

jugadores = [
    {'nombre': 'Brandom', 'edad':22},
    {'nombre': 'Alana', 'edad':23},
    {'nombre': 'Oso', 'edad':24},
    {'nombre': 'Kafai', 'edad':25}
]

suma_edades =  reduce(lambda acumulador, jugador : acumulador + jugador ['edad'], jugadores, 0)
print(suma_edades)