"""Leer de un archivo"""
def leerArchivo():
    manejador = open("texto.txt")
    print("Imprimir cada linea de texto del archivo")
    for linea in manejador:
        print(linea)

    manejador.close()

def main():
   leerArchivo()

if __name__ == "__main__":
    main()
