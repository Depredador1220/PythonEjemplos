"""Suma impares y pares"""

numero = int(input("Introduce un numero: "))
par    = 0
impar  = 0

for i in range(numero):
    if i % 2 == 0:
        par = par + i;

    else:
        impar = impar + i

print(f"Suma de los pares es: {par} y la suma de los impares es: {impar}")
