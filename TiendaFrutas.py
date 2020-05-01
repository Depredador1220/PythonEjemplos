"""Programa Tienda de Frutas"""

fruta = input("Escribe una fruta: ")

if fruta == 'Naranjas':
    print('Las naranjas cuestan $50.00 pesos el kilo')

elif fruta == 'Manzanas':
    print('Las manzanas cuestan $80.00 pesos el kilo')

elif fruta == 'Platanos':
    print('Los Platanos cuestan $60.00 pesos el kilo')

elif fruta == 'Fresas':
    print('Las fresas cuestan $70.00 pesos el kilo')

else:
    print(f'No vendemos esa fruta o esta agotada')
