import random

def guardar_resultado(nombre, intentos):
    """Guarda el nombre y número de intentos en un archivo."""
    with open("resultados.txt", "a") as archivo:
        archivo.write(f"{nombre} adivino en {intentos} intentos.\n")

def jugar():
    nombre = input("¡Hola! ¿Cuál es tu nombre? ")
    print(f"\nBienvenido, {nombre}. ¡Vamos a jugar a Adivina el Número!")
    
    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print("\nHe pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

        while True:
            try:
                intento = int(input("Introduce tu número: "))
                intentos += 1

                if intento < numero_secreto:
                    print("🔼 El número es mayor. Intenta de nuevo.")
                elif intento > numero_secreto:
                    print("🔽 El número es menor. Intenta de nuevo.")
                else:
                    print(f"🎉 ¡Felicidades, {nombre}! Adivinaste el número en {intentos} intentos.")
                    guardar_resultado(nombre, intentos)  # Guarda el resultado
                    break
            except ValueError:
                print("⚠️ Por favor, ingresa un número válido.")

        jugar_de_nuevo = input("\n¿Quieres jugar otra vez? (si/no): ").lower()
        if jugar_de_nuevo != 'si':
            print("¡Gracias por jugar! Hasta la próxima.")
            break

# Ejecutar el juego
jugar()


