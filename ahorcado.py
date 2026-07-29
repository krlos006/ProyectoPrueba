import random

# Base de datos de 50 palabras
BASE_DE_DATOS = [
    "sofia", "jessica", "carlos", "esteban", "trina", "dexter", "yenny", 
    "henry", "mercedes", "alejandro", "betty", "carolina", "alejandra", 
    "daniela", "sarah", "esteban", "celular", "dikiduki", "dariel", "karim", 
    "pantalla", "murcielago", "libro", "cuento", "juguete", "control", "comida", 
    "japon", "corea", "italia", "bolivar", "dolar", "españa", "rafael", "claret", 
    "antonio", "agua", "almuerzo", "desayuno", "ejercicio", "biceps", "burpees", 
    "sentadillas", "boligrafo", "multiplicacion", "division", "computadora", "teclado", 
    "internet"
]

def juego_ahorcado():
    # Seleccionar una palabra aleatoria de la base de datos
    palabra_secreta = random.choice(BASE_DE_DATOS).lower()
    
    letras_adivinadas = set()
    letras_incorrectas = set()
    fallos = 0
    MAX_FALLOS = 5

    print("=" * 50)
    print("        ¡BIENVENIDO AL JUEGO DEL AHORCADO!        ")
    print("=" * 50)
    print(f"Instrucciones: Adivina la palabra. Tienes un máximo de {MAX_FALLOS} fallos.\n")

    while fallos < MAX_FALLOS:
        # Mostrar avance de la palabra
        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(f"Palabra: {' '.join(palabra_mostrada)}")
        print(f"Contador de fallos: {fallos} / {MAX_FALLOS}")
        
        if letras_incorrectas:
            print(f"Letras incorrectas usadas: {', '.join(sorted(letras_incorrectas))}")
        print("-" * 50)

        # Comprobar victoria
        if "_" not in palabra_mostrada:
            print("\n" + "🎉" * 20)
            print(f"¡FELICITACIONES! 🎉 Has adivinado la palabra secreta: '{palabra_secreta.upper()}'")
            print("🎉" * 20)
            return

        # Pedir letra
        letra = input("Ingresa una letra: ").strip().lower()

        # Validaciones de entrada
        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Entrada no válida. Ingresa solo una letra del alfabeto.\n")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print(f"⚠️ Ya habías intentado con la letra '{letra}'. Intenta con otra.\n")
            continue

        # Comprobar la letra
        if letra in palabra_secreta:
            print(f"✅ ¡Correcto! La letra '{letra}' está en la palabra.\n")
            letras_adivinadas.add(letra)
        else:
            fallos += 1
            letras_incorrectas.add(letra)
            print(f"❌ ¡Fallaste! La letra '{letra}' no está en la palabra.\n")

    # Derrota por alcanzar 3 fallos
    print("=" * 50)
    print("💥 ¡GAME OVER! Has alcanzado el límite máximo de 3 fallos.")
    print(f"La palabra secreta era: '{palabra_secreta.upper()}'")
    print("=" * 50)

def main():
    while True:
        juego_ahorcado()
        
        # Bucle para preguntar si quiere volver a jugar
        while True:
            respuesta = input("\n¿Deseas jugar otra vez? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                print("\n" * 2)  # Añade espacio para limpiar la pantalla entre partidas
                break  # Sale del bucle de pregunta y vuelve a iniciar la partida
            elif respuesta in ['n', 'no']:
                print("\n👋 ¡Gracias por jugar! ¡Hasta la próxima!\n")
                return  # Finaliza el programa por completo
            else:
                print("⚠️ Opción no válida. Por favor escribe 's' para continuar o 'n' para salir.")

if __name__ == "__main__":
    main()