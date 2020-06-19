"""Operaciones con Colas"""

from collections import deque

def operacionesColas():
    cola = deque(["Isis", "Fernanda", "Michelle"])
    print(f"Elementos de la cola son: {cola}")
    print("Agregando otros elementos a la cola")
    cola.append("Larrisa")
    cola.append("Diana")
    cola.append("Sarai")
    print(f"Elementos de la cola son: {cola}")
    print(f"Removido el elemento de la cola: {cola.popleft()}")
    print(f"Removido el elemento de la cola: {cola.popleft()}")
    print(f"Los elementos de la cola son {cola}")

def main():
    operacionesColas()

if __name__ == "__main__":
    main()
