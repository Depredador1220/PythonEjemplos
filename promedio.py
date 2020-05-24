"""Sacar el promedio"""

numero   = int(input("Escribe un numero: ")) 
i        = 0
sum      = 0
contador = 0

while i < numero:
    i = i + 1
    sum = sum + i
    contador = contador + 1

promedio = sum / contador

print(f"El promedio de {numero} es {promedio}")
