"""Calcular el tamaño del arco de un angulo"""

import math

class TamArco:
    def __init__(self):
        self.radio = 0;
        self.angulo = 0;

    def CalcularTamArco(self):
        resultado = 2 * math.pi * self.radio * self.angulo / 360
        print(f"El tamaño del arco es: {resultado}")

arco = TamArco()
arco.radio = 9
arco.angulo = 75
print(f"El angulo es {arco.angulo}")
print(f"El radio es {arco.radio}")
arco.CalcularTamArco()
