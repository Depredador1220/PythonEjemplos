"""Funcion que recibe un numero de string como argumentos"""
def encontrar_unico(*palabras):
    for palabra in palabras:
        lista = list(set(palabra))
        print(f"Las letras unicas de la palabra {palabra} es {lista}")

def main():
    encontrar_unico("pandemia", "inmunidad", "vacuna", "coronavirus")

if __name__ == "__main__":
    main()
