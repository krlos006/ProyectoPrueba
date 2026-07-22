#Estructuras de datos

#LISTAS [los valores van en corchetes], permite agregar valores al final de la lista
frutas = ["manzana", "banana", "cereza"]

# Modificación
frutas.append("naranja")  # Agrega al final

''' Para modificar el valor de un elemento en la lista, se puede 
    acceder a él mediante su índice y asignarle un nuevo valor. 
    Los índices comienzan en 0, por lo que el primer elemento tiene 
    índice 0, el segundo tiene índice 1, y así sucesivamente.
'''
frutas[1] = "pera"       # Cambia "banana" por "pera"
print(frutas)  # ['manzana', 'pera', 'cereza', 'naranja']


#TUPLAS (los valores van en paréntesis), 
#no permite agregar valores al final de la tupla

# Creación
coordenadas = (10.48, -66.90)

# Acceso
latitud = coordenadas[0]

#DICCIONARIOS {los valores van en llaves}, 
#permite agregar valores al final del diccionario 
# Creación
usuario = {
    "nombre": "Carlos",
    "edad": 25,
    "lenguajes": ["Python", "Git"]
}

# Acceso y modificación
print(usuario["nombre"])  # Carlos
usuario["edad"] = 26      # Actualizar valor
usuario["email"] = "carlos@example.com" # Agregar nueva clave

#CONJUNTOS {los valores van en llaves},
#no permite agregar valores al final del conjunto

# Creación
numeros = {1, 2, 3, 3, 4}
print(numeros)  # {1, 2, 3, 4} -> Elimina el 3 duplicado automáticamente

# Operación de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}

print("Comienzan los juegos del hambre")
'''Ejercicio 1: Limpiador e Historial de Duplicados
Consigna:
Dado la siguiente lista con datos duplicados:
entradas = [10, 20, 10, 30, 20, 40, 50, 10]'''

# 1. Lista inicial con duplicados
entradas = [10, 20, 10, 30, 20, 40, 50, 10]
print(entradas, "<- Lista inicial")

# 2. Convertimos a set para ELIMINAR duplicados
entradas_sin_duplicados = set(entradas)
print(entradas_sin_duplicados, "<- Valores únicos (gracias al conjunto)")

# 3. Ordenamos la colección
entradas_ordenadas = sorted(entradas_sin_duplicados)

# 4. Convertimos a tupla para CONGELAR/PROTEGER el resultado (Inmutabilidad)
entradas_final = tuple(entradas_ordenadas)
print(entradas_final, "<- Tupla final (ordenada e inmutable)")

'''Ejercicio 2: Gestor de Inventario con Diccionarios
Consigna:
Crea un programa que simule un inventario de tienda utilizando 
un diccionario, donde la clave sea el nombre del producto y el valor 
sea un diccionario secundario con el precio y el stock.'''

