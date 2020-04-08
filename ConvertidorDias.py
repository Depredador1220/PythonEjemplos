'''CONTADOR DE DIAS A OTROS FORMATOS'''

numeroDias         = int(input("Introduce un numero de dias: "))
numeroAnios        = int(numeroDias / 365)
numeroSemana       = int(numeroDias % 365 / 7)
mantenerNumeroDias = int(numeroDias % 365 % 7)
print(f"Años = {numeroAnios}, Semanas = {numeroSemana}, Dias = {mantenerNumeroDias}")

