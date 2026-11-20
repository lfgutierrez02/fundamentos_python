# DICCIONARIOS

# estructura de un diccionario
diccionario = {
    "clave_1": "valor_3",
    "clave_2": "valor_3",
    "clave_3": "valor_3" 
}
print(diccionario)

# diccionario vacio
diccionario_vacio = {}
print(type(diccionario_vacio))

# diccionario con elementos
diccionario_aprendiz = {
    "Nombre": "Luis",
    "Apellido": "Florez",
    "Programa": "ADSO",
    "Ficha": "3233140",
    "Edad": 23
}
print(diccionario_aprendiz)

# obtener un valor del dicionario por la clave
print(diccionario_aprendiz["Programa"])

print(diccionario_aprendiz.get("Programa"))
print(diccionario_aprendiz.get("correo"))

# obtener las claves del diccionario 
print(diccionario_aprendiz.keys()) # dict_keys(['Nombre', 'Apellido', 'Programa', 'Ficha', 'Edad'])

# obtener los valorfes del diccionario
print(diccionario_aprendiz.values()) # dict_values(['Luis', 'Florez', 'ADSO', '3233140', 23])

# obtener la clave y el valor
print(diccionario_aprendiz.items()) # dict_items([('Nombre', 'Luis'), ('Apellido', 'Florez'), ('Programa', 'ADSO'), ('Ficha', '3233140'), ('Edad', 23)])

# como se arregla o crear un nuevo elemento al diccionario
diccionario_aprendiz["Correo"] = "luid@gmail.com"
print(diccionario_aprendiz)

# modificar un valor dfel diccionario
diccionario_aprendiz["Programa"] = "SST"
print(diccionario_aprendiz)

# metodo para actualizar un valor
diccionario_aprendiz.update({"Nombre": "Fernando"})
print(diccionario_aprendiz)

diccionario_aprendiz.update({"Ciudad": "Sogamoso"})
print(diccionario_aprendiz)

# eliminar el ultimo elemento agregado
diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

# elinimar un elemento en especifico
diccionario_aprendiz.pop("Edad")
print(diccionario_aprendiz)

# eliminar tood los elementos
#diccionario_aprendiz.clear()
#print(diccionario_aprendiz)

# comprobar la pertenencia con in 
print("Ficha" in diccionario_aprendiz)
print("telefono" in diccionario_aprendiz)

if "Ficha" in diccionario_aprendiz:
    print("La clave ficha esta dentro del diccionario")
else:
    print("La clave ficha no esta dentro del diccionario")
    
# recorrer un diccionario con for

# recoreer solo las claves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)
    
# recorrer los valores del diccionario
for valores in diccionario_aprendiz.values():
    print(valores)

# recorrer o imprimir las claves y valores del diccionario 
for clave, valores in diccionario_aprendiz.items():
    print(f"{clave} : {valores}")
    
# DICCIONARIOS ANIDADOS 
aprendices = {
    "aprendiz_1": {
        "nombre": "karen",
        "apellido": "Gutierrez",
        "programa": "ADSO"
    },
    "aprendiz_2":{
        "nombre": "jenifer",
        "apellido": "tivaduiza",
        "programa": "SST"
    },
     "aprendiz_3":{
        "nombre": "lizet",
        "apellido": "mora",
        "programa": "SISTEMAS"
    }
}
print(aprendices["aprendiz_2"]["programa"])

# recorrer un diccionario aninado con ciclos for
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}")
    for clave, valores in datos.items():
        print(f"{clave} : {valores}")