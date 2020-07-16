"""Creacion de clase y objeto"""
class Celular:
    def __init__(self):
        print("Este mensaje es del constructor")

    def RecibirMensaje(self):
        print("Recibir mensaje desde el celular")

    def EnviarMensaje(self):
        print("Enviar mensaje desde el celular")

def main():
    nokia = Celular()
    nokia.RecibirMensaje()
    nokia.EnviarMensaje()

if __name__ == "__main__":
    main()
