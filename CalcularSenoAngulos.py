"""Calcular el seno en grados"""

import math

grados  = int(input("Introduce los grados: "))
nterm   = int(input("Introduce el numero de terminos: "))
radians = grados * math.pi * math.pi / 180

def calcularSeno():
    resultado = 0
    numerador = radians
    denominador = 1

    for i in range(1, nterm + 1):
        term_simple = numerador / denominador
        resultado = resultado + term_simple
        numerador = -numerador * radians * radians
        denominador = denominador * (2 * i) * (2 * i + 1)
    return resultado

def main():
    resultado = calcularSeno()
    print(f"El resultado es {resultado}")

if __name__ == "__main__":
    main()
