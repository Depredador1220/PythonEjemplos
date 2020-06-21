"""Regresar multiples valores de una funcion"""
def regresarMultiplesValores():
    monumento = input("Cual es tu monumento preferido: ")
    año = input("Cuando fue construido: ")
    return monumento, año

def main():
    mnt, an = regresarMultiplesValores()
    print(f"Mi monumento favorito es {mnt} y fue construido en {an}")
    resultado = regresarMultiplesValores()
    print(f"Mi monumento favorito es {resultado[0]} y fue construido en {resultado[1]}")

if __name__ == "__main__":
    main()
