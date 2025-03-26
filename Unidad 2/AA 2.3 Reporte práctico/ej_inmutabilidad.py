#Ejemplo 1 inmutabilidad , funcion pura y sn efectos secundarios

varible_global = 10

def aumentar_varible_():
    return varible_global + 1

print(aumentar_varible_())

#Ejemplo 2 inmutabilidad , funcion pura y sn efectos secundarios
def contar_palabras(texto):
    return len(texto.split())  

oracion = "El tema de hoy es la inmutabilidad en Python"
print(contar_palabras(oracion))

#Ejemplo 3 Uso incorrecto de la inmutabildad
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())

#Uso
texto_ejemplo = "Este es un ejemplo semcillo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

#Mutable
contar_palabras_no_funcional("Otro texto de ejemplo")
print(contador_global)