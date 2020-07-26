"""Funcion super()"""

class Pais:
    def __init__(self, nombre_pais):
        self.nombre_pais = nombre_pais

    def detalles_pais(self):
        print(f"El pais mas feliz del mundo es {self.nombre_pais}")

class PaisMasFeliz(Pais):
    def __init__(self, nombre_pais, continente):
        super().__init__(nombre_pais)
        self.continente = continente

    def detalles_pais_feliz(self):
        print(f"El pais mas feliz en el mundo es {self.nombre_pais} y esta en el continente {self.continente}")

def main():
    finlandia = PaisMasFeliz("Finlandia", "Europeo")
    finlandia.detalles_pais_feliz()

if __name__ == "__main__":
    main()
