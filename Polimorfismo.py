"""Polimorfismo"""

class Vehiculo:
    def __init__(self, modelo):
        self.modelo = modelo

    def modelo_vehiculo(self):
        print(f"El nombre del modelo del vehiculo es {self.modelo}")

class Motocicleta(Vehiculo):
    def modelo_vehiculo(self):
        print(f"El nombre del modelo del vehiculo es {self.modelo}")

class Auto(Vehiculo):
    def modelo_vehiculo(self):
        print(f"El nombre del modelo del vehiculo es {self.modelo}")

class Aeroplano:
    pass

def info_vehiculo(vehiculo_obj):
    vehiculo_obj.modelo_vehiculo()

def main():
    ducati = Motocicleta("Ducati-Scrambler")
    beetle = Auto("Volkswagon-Beetle")
    boeing = Aeroplano()

    for each_obj in [ducati, beetle, boeing]:
        try:
            info_vehiculo(each_obj)

        except AttributeError:
            print("Metodo esperado no presentado en el objeto")

if __name__ == "__main__":
    main()

