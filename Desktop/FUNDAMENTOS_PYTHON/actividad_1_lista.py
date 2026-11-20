#Lista de productos (strings)
productos = ["cuaderno", "lapicero", "borrador", "regla", "mochila", "calculadora", "tijeras" ]

# Deben tener exactamente la misma cantidad de elementos que productos
precios = [2.50, 0.75, 0.50, 1.25, 25.00, 15.90, 3.50]

# Lista de cantidades disponibles (enteros)
cantidades = [50, 120, 80, 45, 15, 20, 30]

# Imprimir las tres listas completas
print("Lista de productos:")
print(productos)

print("\nLista de precios:")
print(precios)

print("\nLista de cantidades:")
print(cantidades)

# Mostrar cuántos productos tiene el inventario
print(f"\nEl inventario tiene {len(productos)} productos.")

# Mostrar el tipo de dato de la lista y del primer elemento
print("\nTipo de dato de la lista productos:", type(productos))
print("Tipo de dato del primer elemento (productos[0]):", type(productos[0]))
