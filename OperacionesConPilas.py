"""Operaciones con Pilas"""

pila = []
tamaño_pila = 3

def mostrarElementosPila():
    print("Elementos actuales en la pila: ")

    for elemento in pila:
        print(elemento)

def pushPila(elemento):
    print(f"Colocando {elemento} a la pila")

    if len(pila) < tamaño_pila:
        pila.append(elemento)
    else:
        print("Pila llena")

def popPila():
    if len(pila) > 0:
        print(f"Elimina el elemento de la pila {pila.pop()}")
    else:
        print("Pila vacia")

def main():
    pushPila(1)
    pushPila(2)
    pushPila(3)
    mostrarElementosPila()
    pushPila(4)
    popPila()
    mostrarElementosPila()
    popPila()
    popPila()
    popPila()

if __name__ == "__main__":
    main()
