
#imprimiendo numeros desde una lista
#numeros = [1, 2, 3, 4, 5]
#for numero in numeros:
#    print(f"Imprimo {numero}")
# Ejercicio fizz buzz
for i in range(1, 101):
    if i % 15 == 0:
        print(f"{i} - FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} - Fizz")
    elif i % 5 == 0:
        print(f"{i} - Buzz")
    else:
        print(f"{i}")

#Eliminar numeros repetidos en un arreglo y buscar el numero mas alto
numeros = [10, 20, 10, 30, 20, 40, 50, 10, 50]
#Almaceno en la variable repetidos los numeros repetidos en el arreglo
repetidos = sorted(set(num for num in numeros if numeros.count(num) > 1))

#elimino los numeros repetidos y ordeno el arreglo de mayor a menor para obtener el numero mas alto
numeros_sin_repetir = sorted(list(set(numeros)), reverse=True) #reverse=True para ordenar de mayor a menor
print(f"Dado el arreglo: {numeros}; los numeros repetidos son: {repetidos}, la lista ordenada es: {sorted(numeros_sin_repetir)} y el numero mas alto es: {numeros_sin_repetir[0]}")


#Tablas de multiplicar del 1 al 10
print("Tabla de multiplicar del 1 al 10")
print()
for x in range(1, 11):
    print(f"Tabla del {x}")
    for y in range(1, 11):
        print(f"{x} x {y} = {x * y}")
    print()


# Mostrar elementos de una lista sin comillas ni comas
palabras = ("hola", "mundo", "python", "programacion")
print(f"Palabras: {' | '.join(palabras)}")


