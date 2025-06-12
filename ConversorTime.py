#Conversor de tiempo ✓ Horas a minutos ✓ Minutos a segundos ✓ Días a horas ✓ Semanas a días

def horas_a_minutos(horas):

    return horas * 60
def minutos_a_segundos(minutos):

    return minutos * 60
def dias_a_horas(dias):

    return dias * 24

def semanas_a_dias(semanas):

    return semanas * 7

print("Que seleccion deseas:")
print("1.-Horas a minutos")
print("2.-Minutos a segundos")
print("3.-Dias a horas")
print("4.-Semanas a dias")
opcion = int(input("Selecciona una opcion: "))
if opcion == 1:
    horas = int(input("Introduce las horas: "))
    print(f"{horas} horas son {horas_a_minutos(horas)} minutos")
elif opcion == 2:
    minutos = int(input("Introduce los minutos: "))
    print(f"{minutos} minutos son {minutos_a_segundos(minutos)} segundos")
elif opcion == 3:
    dias = int(input("Introduce los dias: "))
    print(f"{dias} dias son {dias_a_horas(dias)} horas")
elif opcion ==4: 
    semanas = int(input("Introduce las semanas: "))
    print(f"{semanas} semanas son {semanas_a_dias(semanas)} dias")
