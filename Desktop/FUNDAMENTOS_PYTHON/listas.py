# LISTA 

# estructura de una lista
lista = ["dato_1", "dato_2", "dato_3"]
print(type(lista)) # class list

# LISTA MIXTA
lista_mixta = ["hola", 123, 3.14, True, ["ADSO", "SST"]]
print(type(lista_mixta))

# EJERCICIO DE LISTA DE APRENDICES DE ADSO 3233140
# indece          1          2          3       4          5
aprendices = ["miguel", "sebastian", "lizet", "oscar", "jenifer"]
print(aprendices)

# acceder a un elemento de la lista
print(aprendices[2]) 

# modificar un elemento de la lista 
aprendices[0] = "luis"
print(aprendices)

# consultar rangos de elentos en las listas 
print(aprendices[0:3])
print(aprendices[0:4])
print(aprendices[0::2])

# conqatenar o unir listas 
programa_tecnicos = ["sistemas teleinformaticos", "redes"]
programas_tecnologicos = ["ADSO", "Topografia"]

programas_sena = programa_tecnicos + programas_tecnologicos
print(programas_sena)

# extender liatas con estent
nuevos_programas_tecnicos = ["inteligencia artificial", "mineria de datos", "redes"]
programa_tecnicos.extend(nuevos_programas_tecnicos)
print(programa_tecnicos)

# medir la longitud de una lista con len
print(len(programa_tecnicos))
print(len(programas_tecnologicos))

# contar elementos repetidos en una lista con count 
print(programa_tecnicos)
print(programa_tecnicos.count("redes"))

# obtener el indece de un elemento
print(aprendices.index("lizet"))
print(programa_tecnicos.index("mineria de datos"))
print(programas_tecnologicos.index("ADSO"))

# copiar una lista nueva . copy
nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

# agrgar nuevos elementos con la funcion .appedn
nueva_lista_aprendices.append("adriana")
nueva_lista_aprendices.append("aleja")
print(nueva_lista_aprendices)

# agregar un nuevo elementos en una pocicion del indice funcion insert
nueva_lista_aprendices.insert(1, "fernando")
print(nueva_lista_aprendices)

# eliminar un elemento de la lista 

# funcion remove elinima la primera ocurrencia de la lista 
nueva_lista_aprendices.remove("oscar")
print(nueva_lista_aprendices)

# elinimar con pop este elimina segun su indice 
nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)

# limpiar todos los elentos de la lista 
"""nueva_lista_aprendices.clear()
print(nueva_lista_aprendices)"""

# ORDENAR LA LSITA  

#ordenar de forma acententemente de la a-z 

nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

# ordenar desendentemente de la z-a
nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

# buscar elementos en la lista con el operador in 
if "aleja" in nueva_lista_aprendices:
    print("Aleja se encontro en la lista de aprendices")
else:
    print("Aleja no se encontro en la lista de aprendices")
    
busqueda = "aleja" in nueva_lista_aprendices
print(busqueda)  