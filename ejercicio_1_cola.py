"""
Ejercicio 1: Cola
Estructura de Datos - Pilas y Colas

Principio FIFO: el primero en entrar es el primero en salir.
"""

from collections import deque

def ejecutar_cola():
    cola = deque()

    while True:
        print("\n===== MENÚ DE COLA =====")
        print("1. Insertar en cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: escribe un número del 1 al 4.")
            continue

        if opcion == 1:
            try:
                numero = int(input("Ingresa el número que deseas insertar: "))
                cola.append(numero)
                print(f"Se insertó {numero} en la cola.")
            except ValueError:
                print("Error: debes ingresar un número entero.")

        elif opcion == 2:
            if cola:
                eliminado = cola.popleft()
                print(f"Se eliminó el primer elemento: {eliminado}")
            else:
                print("La cola está vacía; no hay elementos para borrar.")

        elif opcion == 3:
            if cola:
                print("Elementos de la cola (primero en salir al inicio):")
                for elemento in cola:
                    print(elemento)
            else:
                print("La cola está vacía.")

        elif opcion == 4:
            print("Has seleccionado salir.")
            break

        else:
            print("Opción no válida. Selecciona una opción del 1 al 4.")

def main():
    while True:
        ejecutar_cola()
        repetir = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ").strip().lower()
        if repetir != "s":
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
