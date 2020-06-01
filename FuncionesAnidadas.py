"""Superficie del area de dos cubos"""

def AgregarCubos(a, b):
    def AreaSuperficieCubo(x):
        return 6 * pow(x, 2)
    return AreaSuperficieCubo(a) + AreaSuperficieCubo(b)

def main():
    resultado = AgregarCubos(2, 3)
    print(f"La superfice del area de los dos cubos es: {resultado}")

if __name__ == "__main__":
    main()
