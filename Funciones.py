"""Funciones"""

def function_sin_argumentos():
    print("Este es una definicion de funcion sin argumentos")

def function_con_un_argumento(mensaje):
    print(f"Este es una definicion de funcion con un {mensaje}")

def main():
    function_sin_argumentos()
    function_con_un_argumento("argumento")

if __name__=="__main__":
    main()
