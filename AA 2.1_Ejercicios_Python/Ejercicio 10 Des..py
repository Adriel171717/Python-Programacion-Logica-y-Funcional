# Definir las ramas y sus puntajes iniciales
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Función para mostrar el título del programa
def mostrar_titulo():
    print("=========================================")
    print("  Sombrero Seleccionador de ISC 🧙‍♂️")
    print("=========================================")
    print("Descubre tu rama ideal en Sistemas Computacionales.")
    print("Responde las siguientes preguntas:\n")

# Mostrar el título del programa
mostrar_titulo()

# Pregunta 1
print("P1) ¿Qué te gusta más?")
print("1. Configurar routers y servidores")
print("2. Diseñar esquemas de bases de datos")
print("3. Desarrollar aplicaciones móviles")
print("4. Programar microcontroladores")
print("5. Crear modelos 3D para videojuegos")
print("6. Organizar equipos y planificar tareas")

respuesta = int(input("Elige una opción (1-6): "))

if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_de_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2
else:
    print("Respuesta inválida. No se asignarán puntos.")

# Pregunta 2
print("\nP2) ¿En qué tipo de proyectos te sientes más cómodo?")
print("1. Optimizar redes de comunicación")
print("2. Analizar y organizar grandes volúmenes de datos")
print("3. Crear interfaces de usuario")
print("4. Trabajar con circuitos electrónicos")
print("5. Diseñar gráficos 3D")
print("6. Liderar equipos de desarrollo")

respuesta = int(input("Elige una opción (1-6): "))

if respuesta == 1:
    redes += 3
elif respuesta == 2:
    bases_de_datos += 3
elif respuesta == 3:
    desarrollo_software += 3
elif respuesta == 4:
    programacion_hardware += 3
elif respuesta == 5:
    modelado_3d += 3
elif respuesta == 6:
    gestion_proyectos += 3
else:
    print("Respuesta inválida. No se asignarán puntos.")

# Pregunta 3
print("\nP3) ¿Qué te parece más interesante?")
print("1. Asegurar la privacidad de los datos en una red")
print("2. Diseñar consultas SQL complejas")
print("3. Desarrollar algoritmos eficientes")
print("4. Programar robots")
print("5. Crear animaciones 3D")
print("6. Gestionar presupuestos y recursos")

respuesta = int(input("Elige una opción (1-6): "))

if respuesta == 1:
    redes += 4
elif respuesta == 2:
    bases_de_datos += 4
elif respuesta == 3:
    desarrollo_software += 4
elif respuesta == 4:
    programacion_hardware += 4
elif respuesta == 5:
    modelado_3d += 4
elif respuesta == 6:
    gestion_proyectos += 4
else:
    print("Respuesta inválida. No se asignarán puntos.")

# Pregunta 4
print("\nP4) ¿Qué habilidad te describe mejor?")
print("1. Resolver problemas de conectividad")
print("2. Organizar información de manera eficiente")
print("3. Escribir código limpio y funcional")
print("4. Entender cómo funcionan los dispositivos electrónicos")
print("5. Crear diseños visuales impactantes")
print("6. Coordinar equipos multidisciplinarios")

respuesta = int(input("Elige una opción (1-6): "))

if respuesta == 1:
    redes += 5
elif respuesta == 2:
    bases_de_datos += 5
elif respuesta == 3:
    desarrollo_software += 5
elif respuesta == 4:
    programacion_hardware += 5
elif respuesta == 5:
    modelado_3d += 5
elif respuesta == 6:
    gestion_proyectos += 5
else:
    print("Respuesta inválida. No se asignarán puntos.")

# Pregunta 5
print("\nP5) ¿Qué te gustaría aprender más?")
print("1. Protocolos de comunicación avanzados")
print("2. Minería de datos y Big Data")
print("3. Frameworks de desarrollo modernos")
print("4. Diseño de circuitos integrados")
print("5. Animación y renderizado 3D")
print("6. Metodologías ágiles y Scrum")

respuesta = int(input("Elige una opción (1-6): "))

if respuesta == 1:
    redes += 6
elif respuesta == 2:
    bases_de_datos += 6
elif respuesta == 3:
    desarrollo_software += 6
elif respuesta == 4:
    programacion_hardware += 6
elif respuesta == 5:
    modelado_3d += 6
elif respuesta == 6:
    gestion_proyectos += 6
else:
    print("Respuesta inválida. No se asignarán puntos.")

# Calcular la rama con el puntaje más alto
puntajes = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos": gestion_proyectos
}

rama_ganadora = max(puntajes, key=puntajes.get)

# Mostrar resultados
print("\n=========================================")
print("Resultados:")
print("=========================================")
for rama, puntaje in puntajes.items():
    print(f"{rama}: {puntaje} puntos")
print("\n¡Tu rama ideal es:", rama_ganadora, "!")