"""Clase Base y Clase Derivada"""

class Futbol:
    def __init__(self, pais, division, no_de_veces):
        self.pais = pais
        self.division = division
        self.no_de_veces = no_de_veces

    def fifa(self):
        print(f"{self.pais} pertenece a la division '{self.division}' de la FIFA ")

class CampeonMundial(Futbol):
    def campeonato_mundial(self):
        print(f"{self.pais} ha sido campeon mundial {self.no_de_veces} veces")

def main():
    alemania = CampeonMundial("Alemania", "UEFA", 4)
    alemania.fifa()
    alemania.campeonato_mundial()

if __name__ == "__main__":
    main()
