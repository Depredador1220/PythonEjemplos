"""Clases con multiples objetos"""

class Aves:
    def __init__(self, nombre):
        self.nombrePajaro = nombre

    def AvesVoladoras(self):
        print(f"{self.nombrePajaro} vuela sobre las nubes")

    def NoVoladoras(self):
        print(f"{self.nombrePajaro} es el ave nacional de Australia")

def main():
    buitre = Aves("Buitre")
    grulla = Aves("Grulla")
    emu = Aves("Emu")
    buitre.AvesVoladoras()
    grulla.AvesVoladoras()
    emu.NoVoladoras()

if __name__ == "__main__":
    main()
