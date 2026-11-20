# estructura de una tuplas
tupla = ("elemento_1", "elentos_2", "elemento_3")
print(type(tupla))

tupla_2 = "a", "b", "c"
print(type(tupla_2))

tupla_3 = ("hola",) # es la como lo que lo hace ser tuple
print(type(tupla_3)) 

tupla_4 = tuple("hola")
print(tupla_4)
print(type(tupla_4)) 


tupla_mixta = ("hola", 123, 3,34, True, [1,2,3])
print(tupla_mixta)

# tuplas de aprendices ADSO
aprendices = ("dayana", "jhon", "oscar", "luis", "pepito", "jhon")
print(aprendices)

# acceder a un elemento de la tupla
print(aprendices[2])

# modificar un elemento de la tupla
#aprendices[0] = "diana"
#print(aprendices) # esto no lo permite

# consultar rangos en la tupla
print(aprendices[0:2])
print(aprendices[1:4])
print(aprendices[1:])

# concatenar dos tuplas
tupla_uno = (1, 2, 3)
tupla_dos = (4, 5, 6)

tupla_suma = tupla_uno + tupla_dos
print(tupla_suma)

# multiplicar tupas
tupla_multiplicada = tupla_uno * 3
print(tupla_multiplicada)

# METODOS DE3 LAS TUPLAS

# medir la longuitud  de la tupla
print(len(aprendices))

# contar los elementos repetio de una tupa
print(aprendices.count("jhon"))

# obtener el indice de un elemento
print(aprendices.index("dayana"))

# modificar una tupla convirtiendola en lista
lenguajes = ("HTML", "CSS", "JAVASCRIPT")
print(lenguajes)
print(type(lenguajes))

lista_lenguajes = list(lenguajes) # se convirtio en una lista
print(lista_lenguajes)
print(type(lista_lenguajes))

lista_lenguajes.append("PYTHON")
print(lista_lenguajes)

lenguajes = tuple(lista_lenguajes)
print(lenguajes)
print(type(lenguajes))

# comprobacion de presenciaq con in 
print("PYTHON" in lenguajes)
print("c++" in lenguajes) 

if "HTML" in lenguajes:
    print("HTML, fue encontrado en la tupla")
else:
    print("HTML, no fue encontrado en la tupla")
    
# empaquetar tuplas
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "TOPOGRAFIA"

tupla_programa = (programa_1, programa_2, programa_3)
print(tupla_programa)
print(type(tupla_programa))

# desempaquetar tupla
tupla_ciudades = ("duitama", "sogamoso", "tunja")
ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades
print(ciudad_1)
print(ciudad_2)
print(ciudad_3)

# reccorrer una tupla con for
for ciudad in tupla_ciudades:
    print(ciudad)