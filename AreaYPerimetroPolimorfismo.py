"""Calcular area y perimetro con Polimorfismo"""

import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        print(f"Area del rectangulo es {self.ancho * self.alto}")

    def perimetro(self):
        print(f"El perimetro del rectangulo es {2 * (self.ancho + self.alto)}")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        print(f"Area del circulo es {math.pi * self.radio ** 2}")

    def perimetro(self):
        print(f"El perimetro del circulo es {2 * math.pi * self.radio}")

def tipo_figura(obj_figura):
    obj_figura.area()
    obj_figura.perimetro()

def main():
    obj_rectangulo = Rectangulo(10, 20)
    obj_circulo = Circulo(10)
    for each_obj in [obj_rectangulo, obj_circulo]:
        tipo_figura(each_obj)

if __name__ == "__main__":
    main()
