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