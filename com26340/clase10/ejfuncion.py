#creo una funcion para sumar dos numeros
def sumaDos(pn,sn):
    res=int(pn) + int(sn)
    return res
def saludar():
    print("hola, bienvenido a nuestro programa!!!!")
# aca inica mi programa
saludar()
n1=input("ingrese un número: ")
n2=input("ingrese otro número: ")
print("la suma de los dos números es: " , sumaDos(n1,n2))