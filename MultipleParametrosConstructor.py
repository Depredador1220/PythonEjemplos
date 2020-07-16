"""Multiples parametros en constructor"""
class Celular:
    def __init__(self, nombre):
        self.nombre_celular = nombre

    def RecibirMensaje(self):
        print(f"Recibir mensaje desde el celular {self.nombre_celular}")

    def EnviarMensaje(self):
        print(f"Enviar mensaje desde el celular {self.nombre_celular}")

def main():
    nokia = Celular("Nokia")
    nokia.RecibirMensaje()
    nokia.EnviarMensaje()

if __name__ == "__main__":
    main()
