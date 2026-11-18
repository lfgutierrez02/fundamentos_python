#Solicitar peso y estatura

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

#Validar que sean valores positivos
if peso <= 0 or estatura <= 0:
    print("Error: El peso y la estatura deben ser valores positivos.")
else: 
    imc = peso / (estatura ** 2)
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    #  Mostrar resultados  
    print(f"\nSu IMC es: {round(imc, 2)}")
    print(f"Clasificación: {clasificacion}")