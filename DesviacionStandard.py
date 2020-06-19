"""Desviacion Standard"""

import math

def estadisticas(lista):
    significado = sum(lista) / len(lista)
    print(f"El significado es: {significado}")
    variacion = 0
    
    for elemento in lista:
        variacion += (elemento - significado)**2
        
    variacion /= len(lista)
    print(f"Variacion es: {variacion}")
    desviacionStandard = math.sqrt(variacion)
    print(f"La desviacion standard es {desviacionStandard}")

def main():
    estadisticas([1,2,3,4])

if __name__ == "__main__":
    main()
