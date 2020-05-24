"""Factorial"""

numero     = int(input("Introduce un numero: "))
factorial = 1 

if numero < 0:
    print("No existe factorial para numeros negativos")

elif numero == 0:
    print(f"El factorial de 0 es 1")

else:
    for i in range(1, numero + 1):
        factorial = factorial * i

print(f"El factorial del numero {numero} es: {factorial}")
