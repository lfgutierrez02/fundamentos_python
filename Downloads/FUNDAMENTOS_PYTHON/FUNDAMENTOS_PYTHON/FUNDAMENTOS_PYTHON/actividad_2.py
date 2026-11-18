# Solicitar las tres calificaciones parciales

nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3

promedio_redondeado = round(promedio, 2)

# Calcular cuántos puntos faltan
puntos_faltantes = 5.0 - promedio

# el estudiante aprueba
aprueba = promedio >= 3.0

# Mostrar todos los resultados de forma legible

print("\n Resultados ")
print(f"Promedio de las tres notas: {promedio_redondeado}")
print(f"Puntos faltantes para alcanzar 5.0: {round(puntos_faltantes, 2)}")
print(f"¿El estudiante aprueba?: {aprueba}")