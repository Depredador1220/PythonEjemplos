"""Programa Calificaciones"""

calificacionFinal = float(input("Escribre tu calificacion final: "))

if calificacionFinal < 0 or calificacionFinal > 1:
    print('Calificacion erronea o fuera de rango')

elif calificacionFinal >= 0.9:
    print('Tu calificacion es A')

elif calificacionFinal >= 0.8:
    print('Tu calificacion es B')

elif calificacionFinal >= 0.7:
    print('Tu calificacion es C')

elif calificacionFinal >= 0.6:
    print('Tu calificacion es D')

else:
    print('Tu calificacion es F')
