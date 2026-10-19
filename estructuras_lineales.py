# ============================================================
# ESTRUCTURAS DE DATOS LINEALES - EJEMPLOS EN PYTHON
# ============================================================
# Tipo de arreglo: Arreglo bidimensional, Cola, Pila y Lista Enlazada
# Ejemplo: Operaciones básicas con cada estructura de datos.
#
# Archivo pensado para ejecutarse directamente en Visual Studio Code.
# Ejecutar con:
#     python estructuras_lineales.py
# ============================================================


# ============================================================
# 1. ARREGLO BIDIMENSIONAL
# Tipo de arreglo: Matriz / arreglo de dos dimensiones
# Ejemplo: Tabla de números organizada en filas y columnas.
# ============================================================

print("\n===== 1. ARREGLO BIDIMENSIONAL =====")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz completa:")
for fila in matriz:
    print(fila)

# Consultar un elemento.
# [1][1] significa fila 1, columna 1.
print("Elemento [1][1]:", matriz[1][1])

# Modificar un elemento.
matriz[1][1] = 50
print("Después de modificar [1][1]:", matriz[1][1])

# Agregar un valor a una posición.
matriz[0][0] = 100
print("Después de cambiar [0][0]:", matriz[0][0])

# Python no elimina una posición individual del arreglo.
# Podemos limpiar su contenido asignándole otro valor.
matriz[2][2] = None
print("Después de limpiar [2][2]:", matriz[2][2])


# ============================================================
# 2. COLA (QUEUE)
# Tipo de estructura: Cola
# Principio: FIFO (First In, First Out)
# Ejemplo: Personas esperando en una fila.
# ============================================================

print("\n===== 2. COLA (QUEUE) =====")

cola = []

# ENQUEUE: agregar elementos al final de la cola.
cola.append("Persona 1")
cola.append("Persona 2")
cola.append("Persona 3")

print("Cola:", cola)

# PEEK: consultar el primer elemento sin eliminarlo.
print("Primero de la cola:", cola[0])

# DEQUEUE: eliminar el primer elemento.
eliminado = cola.pop(0)
print("Elemento atendido:", eliminado)
print("Cola después de atender:", cola)

# Agregar otra persona.
cola.append("Persona 4")
print("Cola final:", cola)


# ============================================================
# 3. PILA (STACK)
# Tipo de estructura: Pila
# Principio: LIFO (Last In, First Out)
# Ejemplo: Una pila de platos.
# ============================================================

print("\n===== 3. PILA (STACK) =====")

pila = []

# PUSH: agregar elementos a la pila.
pila.append("Plato A")
pila.append("Plato B")
pila.append("Plato C")

print("Pila:", pila)

# PEEK: consultar el elemento que está en el tope.
print("Elemento en el tope:", pila[-1])

# POP: eliminar el elemento que está en el tope.
eliminado = pila.pop()
print("Elemento retirado:", eliminado)
print("Pila después de retirar:", pila)

# Agregar otro elemento.
pila.append("Plato D")
print("Pila final:", pila)


# ============================================================
# 4. LISTA ENLAZADA
# Tipo de estructura: Lista enlazada simple
# Ejemplo: Nodos conectados mediante una referencia al siguiente.
# ============================================================

print("\n===== 4. LISTA ENLAZADA =====")


class Nodo:
    """Representa un nodo de la lista enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Crear los nodos.
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

# Conectar los nodos.
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Recorrer la lista.
actual = nodo1

print("Elementos de la lista enlazada:")

while actual is not None:
    print(actual.dato)
    actual = actual.siguiente


# Insertar un nuevo nodo entre 20 y 30.
nuevo = Nodo(25)

nodo2.siguiente = nuevo
nuevo.siguiente = nodo3

print("\nLista después de insertar 25:")

actual = nodo1

while actual is not None:
    print(actual.dato)
    actual = actual.siguiente


# ============================================================
# RESUMEN DE LAS OPERACIONES
# ============================================================
print("\n===== RESUMEN =====")
print("Arreglo bidimensional -> filas y columnas")
print("Cola -> FIFO -> append() / pop(0)")
print("Pila -> LIFO -> append() / pop()")
print("Lista enlazada -> nodos conectados mediante referencias")
print("\nFin de los ejemplos.")
