# Lista inicial con 5 canciones de un género favorito
canciones = [ "Mundo de piedra", "Maquiavelico", "Manana sera otro dia", "Pensando en ti", "Jeremias 17 5" ]

print("Lista inicial:")
print(canciones)
print()

# Métodos en orden: append, insert y extend

# append agregar una canción al final
canciones.append("Es epico")
print("Después de append('Es epico'):")
print(canciones)
print()

# insert agregar otra canción en la segunda posición
canciones.insert(1, "De la vida como una pelicula")
print("Después de insert(1, 'De la vida como una pelicula'):")
print(canciones)
print()

# extend fusionar con la lista de Bonus Tracks
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Después de extend(['Bonus Track 1', 'Bonus Track 2']):")
print(canciones)
print()

# remove y pop

# remove eliminar una canción por su nombre
canciones.remove("Pensando en ti")
print("Después de remove('Pensando en ti'):")
print(canciones)
print()

# pop eliminar la última canción y guardar el valor eliminado
cancion_eliminada = canciones.pop()
print(f"Canción eliminada con pop(): {cancion_eliminada}")
print("Lista después de pop():")
print(canciones)
print()

# sort ordenar alfabéticamente
canciones.sort()
print("Lista ordenada alfabéticamente con sort():")
print(canciones)
print()

# Responder las preguntas usando métodos
print("--- Respuestas ---")

# ¿Cuántas canciones tiene la playlist?
print(f"¿Cuántas canciones tiene la playlist? → {len(canciones)}")

# En qué posición está la primera canción que agregaste
posicion_imagine = canciones.index("Imagine")
print(f"¿En qué posición está 'Imagine' (la primera que agregaste)? → índice {posicion_imagine}")

veces_bonus = canciones.count("Bonus Track 1")
print(f"¿Cuántas veces aparece 'Bonus Track 1'? → {veces_bonus}")