color=input('ingrese un color: ')

if color.lower() =='rojo' or color.lower()=='amarillo' or color.lower()=='azul':
    print(f'{color} es un color primario')
else:
    print(f'{color} no es un color primario')