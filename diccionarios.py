"""Diccionarios"""

def main():
    print("Metodo 1: Construir Diccionarios")
    construirDiccionario = {}

    for i in range(0, 2):
        dic_key = input("Introduce la clave: ")
        dic_val = input("Introduce valor: ")
        construirDiccionario.update({dic_key:dic_val})

    print(f"Diccionario es: {construirDiccionario}")
    
    print("Metodo 2: Construir Diccionarios")
    construirDiccionario = {}

    for i in range(0, 2):
        dic_key = input("Introduce la clave: ")
        dic_val = input("Introduce valor: ")
        construirDiccionario[dic_key] = dic_val

    print(f"Diccionario es {construirDiccionario}")

    print("Metodo 3: Construir Diccionarios")
    construirDiccionario = {}
    i = 0

    while i < 2:
        dict_key = input("Introduce clave: ")
        dict_val = input("Introduce valor: ")
        construirDiccionario.update({dict_key:dict_val})
        i = i + 1
    print(f"Diccionario es {construirDiccionario}")

if __name__ == "__main__":
    main()
