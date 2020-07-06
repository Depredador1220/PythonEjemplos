"""Contar el numero de palabras en un archivo"""
def main():
    ocurrencia = dict()
    total = 0

    with open("texto.txt") as manejador:
        for fila in manejador:
            palabras = fila.rstrip().split()
            total += len(palabras)

            for palabra in palabras:
                ocurrencia[palabra] = ocurrencia.get(palabra, 0) + 1

            print("El numero de veces que la palabra aparece en la sentencia es: ")
            print(ocurrencia)
            print(f"Total de palabras en el archivo son: {total}")

if __name__ == "__main__":
    main()
