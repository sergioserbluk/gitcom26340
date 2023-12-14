'''
nota=int(input("ingrese la calificacion"))
if nota <= 6:
    print("Reprobado")
elif nota>=7 and nota<=8:
    print("Aprobado")
elif nota >=9:
    print("Distinguido")
'''
'''
nota= int(input("Ingrese la calificacion: "))
if nota <= 6 :
    print("La calificacion es desaprobado")
elif nota <= 8 :
    print("La calificacion es aprobado")
elif nota <= 10 :
    print("La calificacion es distinguido")
'''
calif=float(input('ingrese calif: '))
if calif<=6:
    print('desaprobado')
elif calif==7 or calif==8:
    print('aprobado')
elif calif==9 or calif==10:
    print('distinguido')
else:
    print('dato ingresado inválido')