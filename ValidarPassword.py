"""Validacion Contraseña"""

import re

def main():
    minuscula = re.compile(r'[a-z]')
    mayuscula = re.compile(r'[A-Z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[$#@]')
    password = input("Introduce tu password: ")

    if len(password) < 6 or len(password) > 12:
        print("Password invalido, no coinciden")

    elif not minuscula.search(password):
        print("Password invalido, no contiene minusculas")

    elif not mayuscula.search(password):
        print("Password invalido, no contiene mayusculas")

    elif not numero.search(password):
        print("Password invalido, no contiene numero")

    elif not especial.search(password):
        print("Password invalido, no contiene una letra especial")

    else:
        print("Password correcto")

if __name__ == "__main__":
    main()
