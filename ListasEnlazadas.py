# =========================================================
# CLASE QUE REPRESENTA UN NODO
# =========================================================

class Nodo:

    def __init__(self, numero):
        # Guardar el número recibido
        self.numero = numero

        # Apuntar al siguiente nodo
        self.siguiente = None


# =========================================================
# CLASE QUE ADMINISTRA LA LISTA ENLAZADA
# =========================================================

class ListaEnlazada:

    def __init__(self):
        # La lista comienza vacía
        self.cabeza = None

    # -----------------------------------------------------
    # INSERTAR UN NODO AL INICIO
    # -----------------------------------------------------

    def Insertar_Nodo_al_Inicio(self, numero):

        # Crear un nuevo nodo
        nuevo_nodo = Nodo(numero)

        # El nuevo nodo apunta a la antigua cabeza
        nuevo_nodo.siguiente = self.cabeza

        # Actualizar la cabeza de la lista
        self.cabeza = nuevo_nodo

    # -----------------------------------------------------
    # INSERTAR UN NODO AL FINAL
    # -----------------------------------------------------

    def Insertar_Node_al_final(self, numero):

        # Crear un nuevo nodo
        nuevo_nodo = Nodo(numero)

        # Si la lista está vacía, el nodo será la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Comenzar desde el primer nodo
        actual = self.cabeza

        # Avanzar hasta encontrar el último nodo
        while actual.siguiente:
            actual = actual.siguiente

        # Conectar el último nodo con el nuevo nodo
        actual.siguiente = nuevo_nodo

    # -----------------------------------------------------
    # ELIMINAR UN NODO AL INICIO
    # -----------------------------------------------------

    def Eliminar_Nodo_al_Inicio(self):

        # Comprobar si la lista está vacía
        if self.cabeza is None:
            return

        # La segunda posición se convierte en la cabeza
        self.cabeza = self.cabeza.siguiente

    # -----------------------------------------------------
    # ELIMINAR UN NODO AL FINAL
    # -----------------------------------------------------

    def Eliminar_Nodo_al_Final(self):

        # Comprobar si la lista está vacía
        if self.cabeza is None:
            return

        # Si solo existe un nodo, eliminarlo
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        # Comenzar desde el primer nodo
        actual = self.cabeza

        # Avanzar hasta el penúltimo nodo
        while actual.siguiente.siguiente:
            actual = actual.siguiente

        # Desconectar el último nodo
        actual.siguiente = None

    # -----------------------------------------------------
    # IMPRIMIR LA LISTA ENLAZADA
    # -----------------------------------------------------

    def imprimir_ListaEnlazada(self):

        # Comenzar desde la cabeza
        actual = self.cabeza

        # Recorrer todos los nodos
        while actual:

            # Imprimir el número sin saltar de línea
            print(actual.numero, "->", end=" ")

            # Avanzar al siguiente nodo
            actual = actual.siguiente

        # Indicar el final de la lista
        print("None")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

# Crear una lista enlazada
Mi_lista = ListaEnlazada()

# Insertar números al inicio
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)

# Insertar un número al final
Mi_lista.Insertar_Node_al_final(56)

# Mostrar la lista original
print("Lista original:")
Mi_lista.imprimir_ListaEnlazada()

# Eliminar el primer nodo
Mi_lista.Eliminar_Nodo_al_Inicio()

# Mostrar la lista después de eliminar al inicio
print("\nDespues de eliminar el nodo al inicio:")
Mi_lista.imprimir_ListaEnlazada()

# Eliminar el último nodo
Mi_lista.Eliminar_Nodo_al_Final()

# Mostrar la lista después de eliminar al final
print("\nDespues de eliminar el nodo al final:")
Mi_lista.imprimir_ListaEnlazada()


# ==================================================
# Autor: Perez Juarez Javier Antonio
# Actividad: Nombre_del_archivo.py
# Descripción: Desarrollo de la actividad correspondiente.
# ==================================================