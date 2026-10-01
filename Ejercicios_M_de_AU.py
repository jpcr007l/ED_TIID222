
# Ejercicio 1

print ("Ejercicio 1 ")

numeros = [10, 20, 30, 40, 50]

print(numeros[2])

# Ejercicio 2 
    
print ("Ejercicio 2 ")

numeros = [10, 20, 30, 40, 50]

numeros[2] = 100

print(numeros)


# Ejercicio 3

print ("Ejercicio 3 ")

numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)

# Ejercicio 4

print ("Ejercicio 4 ")

numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros)

# Ejercicio 5

print ("Ejercicio 5 ")

numeros = [10, 20, 30, 40, 50]

numeros.append(60)
numeros.append(70)

print(numeros)

# Ejercicio 6

print ("Ejercicio 6 ")

numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5])

# Ejercicio 7

print ("Ejercicio 7 ")

numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros[5][0])

# Ejercicio 8

print ("Ejercicio 8 ")

numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)

# Ejercicio 9

print ("Ejercicio 9 ")

numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros)

# Ejercicio 10

print ("Ejercicio 10 ")

numeros = [10, 20, 30, 40]

numeros = numeros + [50, 60, 70]

print(numeros)

# Ejercicio 11

print ("Ejercicio 11 ")

numeros = [10, 20, 30]

numeros.extend([40, 50, 60])

print(numeros)


# Ejercicio 12

print ("Ejercicio 12 ")

numeros = [10, 20, 30]

otros_numeros = [40, 50, 60]

numeros.extend(otros_numeros)

print(numeros)


# Ejercicio 13

print ("Ejercicio 13 ")

numeros = [10, 20, 30]

numeros[len(numeros):] = [40]

print(numeros)


# Ejercicio 14

print ("Ejercicio 14 ")

calificaciones = [70, 85, 90, 65]

calificaciones.append(95)

calificaciones.insert(2, 80)

print(calificaciones)

# Ejercicio 15

print ("Ejercicio 15 - parte 1")

colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print(colores)

print ("Ejercicio 15 - parte 2")

colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print("Negro")

# Ejercicio 16 

print("Ejercicio 16")

numeros = [10, 20, 30, 40]

numeros.insert(2, 95)
numeros.append(50)
numeros.append(67)

print(numeros)

print(numeros[2])

print(numeros[6])

print("El 95 está en la posición:", 2)
print("El 67 está en la posición:", 6)