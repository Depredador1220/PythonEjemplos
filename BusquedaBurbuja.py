"""Ordenar datos mediante busqueda burbuja"""
def busquedaBurbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                temp = lista[j];
                lista[j] = lista[j+1]
                lista[j + 1] = temp

    print(f"La lista ordenada usando busqueda burbuja es: {lista}")

def main():
    lista = [5, 4, 3, 2, 1, 7, 14, 11]
    busquedaBurbuja(lista)

if __name__ == "__main__":
    main()
