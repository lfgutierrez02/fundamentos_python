# Lista de temperaturas de 14 días (dos semanas)
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

print("Lista completa de temperaturas:")
print(temperaturas)
print()

# Indexación: primer día, último día, día 7 y penúltimo día
# (usando índices positivos y negativos)

print("--- Indexación ---")
print(f"Primer día (índice 0): {temperaturas[0]}")
print(f"Primer día (índice negativo -14): {temperaturas[-14]}")

print(f"Último día (índice 13): {temperaturas[13]}")
print(f"Último día (índice negativo -1): {temperaturas[-1]}")

print(f"Día 7 / mitad (índice 6): {temperaturas[6]}")
print(f"Día 7 / mitad (índice negativo -8): {temperaturas[-8]}")

print(f"Penúltimo día (índice 12): {temperaturas[12]}")
print(f"Penúltimo día (índice negativo -2): {temperaturas[-2]}")
print()

# Slicing
print("--- Slicing ---")

# Primera semana (días 1-7 → índices 0 a 6)
primera_semana = temperaturas[0:7]
print(f"Primera semana (días 1-7): {primera_semana}")

# Segunda semana (días 8-14 → índices 7 a 13)
segunda_semana = temperaturas[7:14]
print(f"Segunda semana (días 8-14): {segunda_semana}")

# Solo los días pares de toda la quincena
dias_pares = temperaturas[1::2]
print(f"Dias pares de la quincena: {dias_pares}")

# Lista en orden invertido
invertida = temperaturas[::-1]
print(f"Temperaturas en orden invertido: {invertida}")
print()

# Promedio de cada semana usando sum() y len() sobre los slices
print("--- Promedios ---")
promedio_semana1 = sum(primera_semana) / len(primera_semana)
promedio_semana2 = sum(segunda_semana) / len(segunda_semana)

print(f"Temperatura promedio de la primera semana: {promedio_semana1:.2f} °C")
print(f"Temperatura promedio de la segunda semana: {promedio_semana2:.2f} °C")
print()

# Bonus: ¿Cuál semana tuvo mayor temperatura promedio?
print("--- Bonus ---")
if promedio_semana1 > promedio_semana2:
    print(f"La primera semana tuvo mayor temperatura promedio ({promedio_semana1:.2f} °C)")
elif promedio_semana2 > promedio_semana1:
    print(f"La segunda semana tuvo mayor temperatura promedio ({promedio_semana2:.2f} °C)")
else:
    print("Ambas semanas tuvieron la misma temperatura promedio")