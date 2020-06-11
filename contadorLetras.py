"""Contador de vocales, consonantes y espacios en blanco"""
def main():
   entrada     = input("Introduce una palabra: ")
   vocales     = 0
   consonantes = 0
   espacios    = 0

   for letras in entrada:
       if(letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u'):
           vocales += 1
       elif "a" < letras < "z":
           consonantes += 1
       elif letras == " ":
           espacios += 1

   print(f"Numero total de vocales: {vocales}")
   print(f"Numero total de consontantes: {consonantes}")
   print(f"Numero total de espacios en blanco: {espacios}")

if __name__ == "__main__":
    main()
