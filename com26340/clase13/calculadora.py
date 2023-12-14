import math
while True:
    try:
        x=int(input("ingrese un num: "))
        break
    except:
        print("debe ingresar un entero!")
while True:
    try:
        y=int(input("ingrese otro num: "))
        break
    except:
        print("debe ingresar un entero!")

print("calculo la raiz")
print(f"la raiz de {x} es {math.sqrt(x)}") 
print(f"la raiz de {y} es {math.sqrt(y)}") 
print(f"calculo la potencia de {x} a {y}")
print(f"la potencia es: { math.pow(x,y) }")