"""
Ejercicio 2: Pila
Estructura de Datos - Pilas y Colas

Principio LIFO: el último en entrar es el primero en salir.
"""

def ejecutar_pila():
    pila = []

    while True:
        print("\n===== MENÚ DE PILA =====")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: escribe un número del 1 al 4.")
            continue

        if opcion == 1:
            try:
                numero = int(input("Ingresa el número que deseas insertar: "))
                pila.append(numero)
                print(f"Se insertó {numero} en la pila.")
            except ValueError:
                print("Error: debes ingresar un número entero.")

        elif opcion == 2:
            if pila:
                eliminado = pila.pop()
                print(f"Se eliminó el elemento de la cima: {eliminado}")
            else:
                print("La pila está vacía; no hay elementos para borrar.")

        elif opcion == 3:
            if pila:
                print("Elementos de la pila (de la cima hacia la base):")
                for elemento in reversed(pila):
                    print(elemento)
            else:
                print("La pila está vacía.")

        elif opcion == 4:
            print("Has seleccionado salir.")
            break

        else:
            print("Opción no válida. Selecciona una opción del 1 al 4.")

def main():
    while True:
        ejecutar_pila()
        repetir = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ").strip().lower()
        if repetir != "s":
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
