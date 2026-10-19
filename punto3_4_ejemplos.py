"""
Ejemplos para los puntos 3 y 4 de la investigación:
3. Sintaxis de los ciclos en Python
4. Relación de los ciclos con las estructuras de datos

Este archivo es de apoyo para tomar capturas de código en Visual Studio Code.
Ejecuta cada ejemplo por separado si deseas mostrar su resultado en la terminal.
"""

# ------------------------------------------------------------
# Punto 3.1: Ciclo while
# ------------------------------------------------------------
print("EJEMPLO 3.1 - CICLO WHILE")
opcion = 0

while opcion != 4:
    print("\nMENÚ")
    print("1. Insertar")
    print("2. Eliminar")
    print("3. Listar")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))

print("Fin del ejemplo while.")

# ------------------------------------------------------------
# Punto 3.2: Ciclo for
# ------------------------------------------------------------
print("\nEJEMPLO 3.2 - CICLO FOR")
elementos = [10, 20, 30]

for elemento in elementos:
    print(elemento)

# ------------------------------------------------------------
# Punto 3.3: Instrucción break
# ------------------------------------------------------------
print("\nEJEMPLO 3.3 - BREAK")

while True:
    respuesta = input("Escribe S para salir: ").upper()
    if respuesta == "S":
        break

print("El ciclo terminó con break.")

# ------------------------------------------------------------
# Punto 3.4: Instrucción continue
# ------------------------------------------------------------
print("\nEJEMPLO 3.4 - CONTINUE")

for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

# ------------------------------------------------------------
# Punto 4.1: Cola (FIFO)
# ------------------------------------------------------------
print("\nEJEMPLO 4.1 - COLA FIFO")
from collections import deque

cola = deque()
cola.append(25)
cola.append(40)
cola.append(60)
print("Cola después de insertar:", list(cola))
primero = cola.popleft()
print("Elemento retirado:", primero)
print("Cola actual:", list(cola))

# ------------------------------------------------------------
# Punto 4.2: Pila (LIFO)
# ------------------------------------------------------------
print("\nEJEMPLO 4.2 - PILA LIFO")

pila = []
pila.append(25)
pila.append(40)
pila.append(60)
print("Pila después de insertar:", pila)
ultimo = pila.pop()
print("Elemento retirado:", ultimo)
print("Pila actual:", pila)
