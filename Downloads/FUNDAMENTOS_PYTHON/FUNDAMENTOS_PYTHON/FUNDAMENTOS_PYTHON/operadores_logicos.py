# OPERADORES LOGICOS
# operador AND
print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false

# operador or
print(True or True) # true
print(True or False) # true
print(False or True) # true
print(False or False) # true

# operador not
print(not False) # false
print(not True) # true

# EJERCICIO CON AND

print(5 > 3 and 2 < 4) # true
print(5 > 3 and 5 < 4) # false
print(2 > 3 and 2 < 4) # false
print(2 > 3 and 5 < 4) # false

# ejercicio con or
print(3 == 3 or 2 < 4) # true
print(2 >= 3 or 3 != 3) # true
print(2 != 3 or 5 < 10) # true
print(10 < 5 or 5 == 6) # false

# EJERCICIO CON NOT 

print(not 2 == 2)
print(not 2 > 3)