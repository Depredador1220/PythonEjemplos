"""Numeros Primos"""

numero = int(input("Introduce un numero > 1: "))
primo  = True  

for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f"{numero} es un numero primo")

else:
    print(f"{numero} no es un numero primo")
