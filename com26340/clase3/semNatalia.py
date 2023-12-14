color= input("Ingrese el color del semáforo: ")

if color.lower()=="verde":
    print("El semáforo esta en verde, puede pasar")
elif color.lower()=="amarillo":
    print("El semáforo esta en amarillo, debe esperar.")
elif color.lower()=="rojo":
    print("El semáforo esta en rojo, no puede pasar")
else:
    print("Usted ingreso un color incorrecto)")