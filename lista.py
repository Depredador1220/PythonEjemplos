"""Entrada de usuario como una lista"""
elementos_lista = input("Introduce elementos de la lista separados por un espacio: ").split()
print(f"Los elementos de la lista son: {elementos_lista}")

elementos_de_lista = []
total_elementos = int(input("Introduce el total de elementos: "))

for i in range(total_elementos):
    elemento = input("Introduce un elemento: ")
    elementos_de_lista.append(elemento)


print(f"Elementos de la lista son {elementos_de_lista}")
