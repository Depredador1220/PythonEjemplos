"""Excepciones"""

while True:
    try:
        numero = int(input("Introduce un numero: "))
        print(f"El numero que ingresaste es {numero}")
        break

    except ValueError:
        print("Error, no ingresaste un numero")
