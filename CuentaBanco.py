"""Simular Cuenta de Banco"""

class CuentaBanco:
    def __init__(self, nombre):
        self.usuario = nombre
        self.balance = 0.0

    def MostrarBalance(self):
        print(f"{self.usuario} tiene un balance de {self.balance} pesos mexicanos")

    def RetirarDinero(self, cantidad):
        if cantidad > self.balance:
            print(f"Tu no tienes suficientes fondos en esta cuenta")
        else:
            self.balance -= cantidad
            print(f"{self.usuario} va a retirar una cantidad de {self.balance} pesos mexicanos")

    def DepositarDinero(self, cantidad):
        self.balance += cantidad
        print(f"{self.usuario} ha depositado una cantidad de {self.balance} pesos mexicanos")

def main():
    cuenta = CuentaBanco("Kensho")
    cuenta.DepositarDinero(1000)
    cuenta.MostrarBalance()
    cuenta.RetirarDinero(500)
    cuenta.MostrarBalance()

if __name__ == "__main__":
    main()
