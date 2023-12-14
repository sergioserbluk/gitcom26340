color=input('ingrese un color').lower()
if color=='rojo'or color=='amarillo' or color=='azul':
    print(f'{color} es un color primario')
elif color=='violeta' or color=='verde' or color=='anaranjado':
    print(f'{color} es un color secundario')
else:
    print(f'{color} no es un color primario ni secundario')