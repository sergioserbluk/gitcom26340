'''
co = input ("Ingrese un color primario: ") 
co= co.lower()
if co.lower()=="rojo":
    print("El color es primario")
elif co.lower()=="azul":
    print("El color es primario")
elif co.lower()=="Amarillo":
    print("El color es primario")
else:
    print("El color es secundario")
    '''
co = input ("Ingrese un color primario: ") 

if co.lower()=="rojo":
    print("El color es primario")
elif co.lower()=="azul":
    print("El color es primario")
elif co.lower()=="Amarillo":
    print("El color es primario")
elif co.lower()=="verde":
    print("El color es secundario")
elif co.lower()=="naranja":
    print("El color es secundario")
elif co.lower()=="violeta":
    print("El color es secundario")
else:
    print("El color no es primario o ni secundario")