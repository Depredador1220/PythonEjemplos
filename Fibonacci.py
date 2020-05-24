"""Serie Fibonacci"""

nterminos = int(input("Escribe un numero: ")) 
actual    = 0
anterior  = 1
siguiente = 0
contador  = 0
sig_term  = 0

if nterminos <= 0:
    print('Introduce un numero positivo')

elif nterminos == 1:
    print("Secuencia Fibonacci: ")
    print('0 ')

else:
    print("Secuencia Fibonacci: ")
    while contador < nterminos:
        print(sig_term)
        actual = sig_term
        sig_term = anterior + actual
        anterior = actual
        contador += 1
