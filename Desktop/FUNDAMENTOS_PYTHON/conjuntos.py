# CONJUNTOS

# ESTRUCTURA DE UN CONJUNTO
conjunto = {"elemento_1", "elementos_2", "elemento_3"}
print(type(conjunto)) # <class 'set'>

# declarar un conjunto vacio 
conjunto_2 = set()
print(type(conjunto_2)) # <class 'set'>

# crear un conjunto no permite elementos duplicados
programas = {"ADSO", "SST", "MINERIA", "ADSO", "SST"}
print(programas) # {'MINERIA', 'ADSO', 'SST'}

# metodos de los  conjuntos
frutas = {"mango", "guayaba", "mora", "manzana", "mandarina"}

# agregar ub nuevo elemento al conjunto
frutas.add("fresas")
print(frutas) #{'mora', 'fresas', 'guayaba', 'mango'}

frutas.add("mora")
print(frutas)

# eliminar un elemento del conjunto

# motodo .remove
frutas.remove("mango")
print(frutas)

# funcion discar es un metodo de eliminar
frutas.discard("mora")
print(frutas)

frutas.discard("pera")
print(frutas)

# metodo pop 
elemento = frutas.pop()
print(elemento)
print(frutas)

# funcion clear es para eliminar todos los elementos
#frutas.clear()
#print(frutas)

# eliminara todo el conjunto
#del frutas
#print(frutas)

# verificar loa pertenencia de un elemento en un conjunto
aprendices = {"jenifer", "andres", "pepito"}

print("jenifer" in aprendices)
print("juan" in aprendices)

# OPERACIONES DE LA TEORIA DE CONJUNTOS
aprendices_formacion = {"diana", "lizet", "alejandra", "adriana", "jenifer"}
aprendices_apoyo = {"diana", "adriana", "luis", "sebastian", "oscar"}

# union extrae todos los elementos de los dos conjuntos
union_aprendices = aprendices_formacion | aprendices_apoyo
print(union_aprendices)

union_aprendices = aprendices_formacion.union(aprendices_apoyo)
print(union_aprendices)

# traer los elemnetos que se repiten
interpcion_aprendices = aprendices_formacion & aprendices_apoyo
print(interpcion_aprendices)

interpcion_aprendices = aprendices_formacion.intersection(aprendices_apoyo)
print(interpcion_aprendices)

# diferencia
diferencia_aprendices = aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices)

diferencia_aprendices = aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices)

# diferencia cimetrica
diferencia_cimetrica = aprendices_formacion ^ aprendices_apoyo
print(diferencia_cimetrica)

diferencia_cimetrica = aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(diferencia_cimetrica)