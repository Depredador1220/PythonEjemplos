"""Poblar tuplas"""
elementosTupla = ()
totalElementos = int(input("Introduce un numero de elementos: "))

for i in range(totalElementos):
    entrada = int(input("Introduce un numero: "))
    elementosTupla += (entrada,)

print(f"Elementos agregados a la tupla son: {elementosTupla}")

lista = []
totalElementos = int(input("Introduce el total de numero de elementos: "))

for i in range(totalElementos):
    elemento = input("Introduce un elemento a agregar: ")
    lista.append(elemento)

elementosTupla = tuple(lista)
print(f"Tupla de elementos son: {elementosTupla}")
