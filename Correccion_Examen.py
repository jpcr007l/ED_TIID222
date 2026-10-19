
# Ejercicio 11

Matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

# Línea de código para agregar la siguiente fila: [39, 22, 69, 17]
Matriz.append([39, 22, 69, 17])

# Línea de código correspondiente para imprimir la fila 2
print(Matriz[2])

for i in Matriz:
    if 18 in i:
        print(f"18 se encuentra en la fila: {i}")
        break 

for filas in Matriz :
    for numeros in filas:
        if numeros == 3 :
            print(f"3 encontrado en {filas}")


matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

for fila in range(len(matriz)):
    for elemento in matriz[fila]:
        if elemento == 61:
            print(f"61 encontrado en la fila {fila}")

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == 18:
            print(f"18 encontrado en la fila {fila} columna {columna}")



# Declarar una cola vacía
cola = []

# Agregar los elementos A, B, C y D
cola.extend(["A", "B", "C", "D"])
cola.pop(0)

# Mostrar la cola en pantalla
print("Cola:", cola)

# Ejercicio de PILA
pila = ["Plato A", "Plato B", "Plato C"]
print("Pila actual:", pila)

desempilar = pila.pop()
print("Elemento retirado:", desempilar)
print("Pila después del pop:", pila)

pila.append("Plato D")
print("Pila final:", pila)


print("Pila actual:", pila)
desempilar = pila.pop()
print("Pila después del pop:", pila)


numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])
print(numeros[5])


numeros = [10, 20, 30, 40]
numeros.insert(____, ____)
print(numeros)
