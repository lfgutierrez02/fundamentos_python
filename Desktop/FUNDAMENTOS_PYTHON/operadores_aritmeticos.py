# OPEREADORES ARITMETICOS
a = 10
b = 3

#suma
suma = a + b
print(f" la suma de {a} y {b} es: {suma}")

# resta 
resta = a - b
print(f" la resta de {a} y {b} es: {resta}")

# multiplicacion
multiplicacion = a * b
print(f" la multiplicacion de {a} y {b} es: {multiplicacion}")

# division
division = a / b
print(f" la division de {a} y {b} es: {division}")

# divicion entera

division = a // b
print(f" la division de {a} y {b} es: {division}")

# modulo o residuo
modulo = a % b
print(f" el modulo de {a} y {b} es: {modulo}")

# potencia o exponenciacion
potencia = a ** b
print(f" la potencia de {a} elevado a {b} es: {potencia}")

# presedencia de operadores 
resultado = a + b * 2
print(f" El resultado de la operacion es: {resultado}")

resultado_2 = (a + b ) * 2
print(f" El resultado de la operacion es: {resultado_2}")

resultado_3 = a * b // 3
print(f" El resultado de la operacion es: {resultado_3}")

ejercicio = ((a + b) * (a - b) / (a * b )) - ((a ** b) % 3)
print(f" El resultado de la operacion es: {ejercicio}")

# LIBRERIAS DE PYTHON 
import math
print(math.pi)
print(math.e)
print(math.sqrt(16))

import random
print(random.random()) # jenera numeros aleatorios