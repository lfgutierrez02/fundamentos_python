print("Hola mundo")

#  escritura de las variables ------------------------- 
#camescap

aprendizSena = "sena"

AprendizSena = "sena"
#sneckes
aprendiz_sena = "sena"

#reglas d elas variables no deja iniciar con numeros ni carracteres especiales,
# las mayusculas y minusculas, palabras reservadas

nombre_completo = "luis gutierrez"

#TIPOS DE DATOS PRIMITIVOS --------------------
nombre = "Luis"
print(type(nombre))  #STR

edad = 23
print(type(edad)) # INT

altura = 1.78
print(type(altura)) #FLOAT

activo = True
print(type(activo)) #BOOL

# DATO COMPLEJO

conplejo = 2+3j
print(type(conplejo)) 

byte = b"hola"
print (type(byte))

nulo = None
print(type(nulo))

# TIPOS DE DATOS ESTRUCTURAS--------------------

lista = ["python", "javascript", "css"]
print(type(lista)) #LIST

conjunto = {"html", "css"}
print(type(conjunto)) #SET

tupla = ("java", "c#")
print(type(tupla))

diccionario = {"nombre": "luis", "edad": 23}
print(type(diccionario))

rango = range(5)
print(type(rango))

# CONVERCION DE TIPOS DE DATOS O CASTEAR --------------------

#casteo de entero a texto
telefono = 3147849345
print(type(telefono), telefono) #int

telefono_str = str(telefono)
print(type(telefono_str), telefono_str) # str

# casteo de texto a entero
cedula = "10027627784"
print(type(cedula), cedula)

cedula_int = int(cedula)
print(type(cedula_int), cedula_int)

#casteo de buliano a entero
matriculado = False
print(type(matriculado))

matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int) # TIPO ENTERO

# casteo de decimal a entero
promedio = 4.13
print(type(promedio), promedio)

promedio_int = int(promedio)
print(type(promedio_int), promedio_int) 

# casteo entero a decimal

edad = 23
print(type(edad), edad)

edad_float = float(edad)
print(type(edad_float), edad_float)

#casteo de enetero a guliano

activo = 1
print(type(activo))

activo_bool = bool(activo)
print(type(activo_bool), activo_bool)

#casteo de goliano aun decimal

beneficio = True
print(type(beneficio))

beneficio_float = float(beneficio)
print(type(beneficio_float), beneficio_float)

#casteo de decimal a guliano

descuento = 10.5
print(type(descuento), descuento)

descuento_bool = bool(descuento)
print(type(descuento_bool), descuento_bool)

#COMENTARIOS -------- este es un comentario de una sola linea
""" este es un comentario der variar
lineas que se utiliza para explicar el 
codigo con mas detalle"""

#INDENTACION ES PYTHON
#condional if

if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")
    

# entrada de datos

nombre_completo = input("ingresa tu nombre completo: ")
programa = input("Cual es tu programa de formacion: ")

print("hola", nombre_completo, "Bienvedido al curso de python")

print("hola mi nombre es:", nombre_completo, "y estoy en el programa de:", programa)
        
# impresion con formato f-string

print(f" Hola mi nombres es: {nombre_completo}, y estoy en el programa de: {programa}") # forma en la cual se debe hacer

