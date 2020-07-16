"""Parametros por default en constructor"""

class Perro:
    def __init__(self, raza="Chihuahua", color="Blanco"):
        self.raza = raza
        self.color = color

    def RazaPerro(self):
        print(f"La raza del perro es: {self.raza}")

    def ColorPerro(self):
        print(f"El color del perro es {self.color}")

def main():
    dante = Perro()
    dante.RazaPerro()
    dante.ColorPerro()

if __name__ == "__main__":
    main()
