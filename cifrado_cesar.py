# Función que cifra un texto aplicando el cifrado César
def cifrar(texto, desplazamiento):
    # Variable que acumulará el texto cifrado resultante
    resultado = ""
    # Recorre cada carácter (letra, número, símbolo, espacio) del texto de entrada
    for char in texto:
        # Comprueba si el carácter actual es una letra del alfabeto (a-z o A-Z)
        if char.isalpha():
            # Define el valor base ASCII (65 para 'A') si es mayúscula, o (97 para 'a') si es minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Desplaza la letra: obtiene su posición en el alfabeto, suma el desplazamiento,
            # aplica módulo 26 para dar la vuelta al final del abecedario y la convierte de nuevo a carácter
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            # Si no es letra (espacio, número, puntuación), se agrega tal cual sin cifrar
            resultado += char
    # Devuelve el texto cifrado completo
    return resultado


# Función que descifra un texto cifrado: usa cifrar con el desplazamiento negativo
def descifrar(texto, desplazamiento):
    # Descifrar equivale a cifrar con el desplazamiento inverso (negativo)
    return cifrar(texto, -desplazamiento)


# Función principal que ejecuta el programa por consola
def main():
    # Muestra el título del programa
    print("=== CIFRADO CESAR ===")
    # Pide al usuario el texto que desea cifrar o descifrar
    texto = input("Texto: ")
    try:
        # Pide el desplazamiento y lo convierte a número entero (int)
        desplazamiento = int(input("Desplazamiento: "))
    except ValueError:
        # Se ejecuta si el usuario no ingresa un número entero válido
        print("El desplazamiento debe ser un numero entero.")
        # Termina la ejecución de la función main si el desplazamiento no es válido
        return

    # Pide la operación a realizar (Cifrar o Descifrar) y la convierte a minúsculas
    opcion = input("(C)ifrar o (D)escifrar? ").lower()
    # Si el usuario eligió "c", se cifra el texto y se muestra el resultado
    if opcion == "c":
        print("Resultado:", cifrar(texto, desplazamiento))
    # Si el usuario eligió "d", se descifra el texto y se muestra el resultado
    elif opcion == "d":
        print("Resultado:", descifrar(texto, desplazamiento))
    # Si ingresa cualquier otra opción, se muestra un mensaje de error
    else:
        print("Opcion no valida.")


# Punto de entrada: solo se ejecuta main() si el script se ejecuta directamente
if __name__ == "__main__":
    main()
