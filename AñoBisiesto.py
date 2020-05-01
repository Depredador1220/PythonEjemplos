"""Programa que determina si el año es bisiesto"""

año = int(input("Introduce un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f"{año} es un año bisiesto")
        else:
            print(f"{año} no es un año bisiesto")
    else:
        print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")
