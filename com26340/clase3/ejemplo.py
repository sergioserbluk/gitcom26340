#escribir un programa que permita ingesar el nombre de un 
#animal.
#luego pida mas datos para especificar.
animal=input("ingrese en nombre del timpo de animal que tien por mascota")
if animal=="perro":
    print("el perro es el mejor amigo del hombre")
    lp=input("ingrese el largo del pelo largo/medio/corto")
    if lp=="largo":
        print("espa preparado para zonas frias")
    elif lp=="corto":
        print("es un animal para zonas calurosas")
    else:
        print("se adapta a un gran rango de temperaturas")
elif animal=="gato":
    print("son mascotas muy independientes ")
    color=input("ingresa su color, negro, atigrado, con manchas, blanco")
    if color=="negro":
        print("son felinos con instinto bien marcado")
    elif color=="atigrado":
        print("suelen tener mal humor")
    elif color=="con manchas" or color=="blanco":
        print("son mimosos")
else:
    print("Lo siento, no tengo datos sobre ese tipo de mascotas.")
print("adios")