# CONDICIONALES IF
# ESTRUCTURA DEL CONDICIONAL IF ES "if" 

if True:
    print(" Se ejecuta la instruccion")

# ejemplo

edad = 23
if edad > 18:
    print(" Eres un adulto")
else:
    print(" Eres un joven")    
    
# estructura del elif

if False:
    print(" La primera condicion")
elif True:
    print(" Segunda condicion")
elif False:
    print(" Tercera condiciopn")
else:
    print(" Todas las condiciones son falsas")
    
# EJERCICIO CLASIFICACION DE EDAD

edad = 23 

if edad < 18:
    print(" Eres menor de edad")
elif edad >= 18 and edad < 65:
    print(" Eres un adulto")
else:
    print(" Eres un adulto mayor")
    
# ESTRUCTURA CONDICIONAL ANIDADOS

if True:
    if True:
        print("Se ejecuta la instruccion")
    elif True:
        print("se ejecuta la instruccion")
    else:
        print("no se ejecuta la instruccion")
else:
    print("no se ejecuta la instruccion")
    
# EJERCICIO CLASIFICACION DE EDAD IF ANIDADO

edad = 12

if edad < 18:
    if edad > 12 and edad < 18:
        print("Adolecente")
    else:
        print("Niño")
else:
    if edad >= 18 and edad < 60:
        print("Adulto")
    else:
        print("Adulto mayor")
        
# EJECICIO DEL PARTIDO CON IF

marcador_colombia = int(input("Ingrese el marcador de colombia: "))
marcador_chile = int(input("Ingrese el marcador de chile: "))

if marcador_colombia > marcador_chile:
    print("Colombia es el ganador del partido")
elif marcador_colombia == marcador_chile:
    print("Quedamos empatados")
else:
    print("perdimos el partido")
    
    
# OPERADOR TERNARIO

numero = 4
if numero% 2 == 0:
    print("el nimero es par")
else:
    print("el numero es impar")
print("el numero es par" if numero% 2 == 0 else "el numero es impar")