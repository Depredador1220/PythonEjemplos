"""Ordenar datos mediante busqueda burbuja"""
def leerEntrada():
    clave = int(input("Introduce el elemento clave para la busqueda: "))
    return clave

def busquedaLineal(clave):
    lista = [10, 20, 30, 40, 50]
    encontrado = False

    for indice in range(len(lista)):
        if lista[indice] == clave:
            encontrado = True
            break

    if encontrado:
        print(f"{clave} encontrado en la posicion {indice + 1}")
    else:
        print("Elemento no encontrado en la lista")

def main():
    clave = leerEntrada()
    busquedaLineal(clave)

if __name__ == "__main__":
    main()
