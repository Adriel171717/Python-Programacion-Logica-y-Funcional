asignatura_VII = ["Programacion BackEnd"]
#print(asignatura_VII[0])

asignaturas = asignatura_VII + ["Programacion logica"]
##print(asignaturas)

def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignatura_VII, "Programacion FrontEnd"))