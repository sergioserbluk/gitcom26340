
'''
max=numusu=float(input('ingrese un número: '))
a=1
while a<3:
    numusu=float(input('ingrese un número: '))
    if numusu>max:
        max=numusu
    a+=1
print(f'el mayor es {max}')
'''
'''
n=int(input("ingrese un numero:  "))
n1=int(input("ingrese otro numero:  "))
n2=int(input("ingrese otro numero:  "))

if n > n1 and n > n2 :
    print (f"{n} es mayor a {n1} y {n2}")

elif n1 > n and n1 > n2 :
    print (f"{n1} es mayor a {n} y {n2}")

elif n2 > n and n2 > n1 :
    print (f"{n2} es mayor a {n} y {n1}")

else:
    print ("Los numeros son iguales")
'''
num=int(input("Ingrese Numero: "))
for x in range(1,4):
    if x==1:
        num_max=num
    elif x!=1:
     num_2=int(input("ingrese un numero: "))
     if num_max<num_2:
        num_max=num_2
print(f"el mumero mayor es {num_max}")
