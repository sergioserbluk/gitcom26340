import os
def menu():
    os.system("cls")
    print("*************menu************")
    print("1 para sumar")
    print("2 para restar")
    print("3 para multi")
    print("4 para divid")
    print("5 para salir")
    op=int(input("seleccione una opcion: "))
    return op
def sumar(pn, sn):
    res = pn + sn
    return res
def restar(pn, sn):
    res = pn - sn
    return res
def multiplicar(pn, sn):
    res=pn * sn
    return res
def dividir(pn,sn):
    try: #habilito el control de errores
        res=pn/sn
        return res
    except: #doy tratamiento al error
        print("no se puede dividir por 0")
        return
#programa principal
resp="N"
while True:
    op=menu()
    if op != 5:
        if resp=="N":
            n1=float(input("ingrese un num: "))
        else:
            n1=res
        n2=float(input("ingrese otro num: "))
    else:
        break
    if op==1:
        res=sumar(n1,n2)
        print(f"el reultado de sumar {n1}  y {n2} es: " ,res)
        input("presione enter para continuar...")
    elif op==2:
        res=restar(n1,n2)
        print(f"el reultado de restar {n1}  y {n2} es: ", res)
        input("presione enter para continuar...")
    elif op == 3:
        res=multiplicar(n1,n2)
        print(f"el resultado de multiplicar {n1} por {n2} es: {res}")
        input("presione enter para continuar...")
    elif op == 4:
        res=dividir(n1 , n2)
        print(f" el resultado de dividir {n1} y {n2} es {res}")
        input("presione enter para continuar...")
    elif op ==5:
        print("adios!")
        break
    else:
        print("opcion incorrecta...")
        input("presione enter para continuar...")
    resp=input("quiere seguir operando con este resultado? S/N")


