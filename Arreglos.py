# Se declara un arreglo con cinco números enteros.
numeros = [10, 20, 30, 40, 50]

# Se imprime el arreglo completo para mostrar todos sus elementos.
print (numeros) # Imprime el arreglo completo

# Se accede a elementos individuales del arreglo por su posición.
print (numeros[0]) # Imprime el primer elemento del arreglo
print (numeros[1]) # Imprime el segundo elemento del arreglo
print (numeros[2]) # Imprime el tercer elemento del arreglo
print (numeros[3]) # Imprime el cuarto elemento del arreglo
print (numeros[4]) # Imprime el quinto elemento del arreglo

# Se cambia el valor de una posición específica del arreglo.
numeros[3] = 35
print (numeros[3]) # Imprime el cuarto elemento del arreglo (ahora es 35)

# Se agrega un nuevo valor al final del arreglo con append().
numeros.append(60)
print(numeros)

# Se elimina un valor del arreglo por su contenido con remove().
numeros.remove(35)
print(numeros)

# Se elimina un valor del arreglo por su posición con pop().
numeros.pop(4)
print(numeros)

# Se declara un arreglo de cadenas para guardar nombres de frutas.
fruta = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]

# Se elimina una fruta por su posición dentro del arreglo.
fruta.pop(4)
print(fruta)

# Se elimina una fruta por su nombre usando remove().
fruta.remove("Manzana")
print(fruta)

# Separador para indicar la parte nueva del ejercicio.
#|-----------------------------------------------------21-09-26----------------------------------------------|

#Declaracion  de arreglo vacio 

arreglo = []

print (arreglo)

#Ejercicio -> LLenar un arreglo utilizando append

"""
n = int(input("Ingrese el tamaño del arreglo"))

print(n)

for i in range (n):
    dato = int(input("Ingrese un valor: "))
    arreglo.append(dato)

"""

#Ejericio -> LLenar un arreglo sin utilizar append

"""
n = int(input("Ingrese el tamaño del arreglo"))

arreglo = [0] * n  # Inicializa un arreglo de tamaño n con ceros

for i in range (n):
    dato = int(input("Ingrese un numero: "))
    arreglo [i] = dato

"""

#Ejercicio Escribe un programa que rellene un array de 15 elementos con numeros enteros comprendidos entre 0 y 500 (Pedir numeros).
#Segun el siguiente criterio: si el numero que hay en una posicion del array es multiplo de 5, se deja igual y si no, se cambia por el siguiente multiplo de 5 que exista a partir de el.

# Se crea una lista vacía para guardar los 15 números que ingrese el usuario.
arreglo = []

# Este ciclo se repite 15 veces, una por cada posición del arreglo.
for i in range(15):
    # Se usa un ciclo while para repetir la entrada hasta que el número sea válido.
    while True:
        # Se solicita el número y se muestra la posición actual.
        dato = int(input(f"Ingrese el numero {i + 1} de 15 (entre 0 y 500): "))

        # Si el número está dentro del rango solicitado, se guarda en el arreglo.
        if 0 <= dato <= 500:
            arreglo.append(dato)
            break

        # Si el número está fuera del rango, se muestra un mensaje de error y se vuelve a pedir.
        print("Error: el numero debe estar entre 0 y 500.")

# Mostrar el arreglo antes de hacer la modificación.
print("Arreglo original:", arreglo)

# Recorrer el arreglo y convertir los números que no sean múltiplos de 5 al siguiente múltiplo de 5.
for i in range(len(arreglo)):
    if arreglo[i] % 5 != 0:
        arreglo[i] = ((arreglo[i] // 5) + 1) * 5

# Mostrar el arreglo ya modificado.
print("Arreglo final:", arreglo)


