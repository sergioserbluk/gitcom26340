color= input('ingrese un color ')

if color.lower() == 'rojo' or color.lower() == 'azul'or color.lower() == 'amarillo':
    print(f'el color {color} ingresado es primario')

else:
    print(f'{color} no es un color primario')

if color.lower() == 'naranja' or color.lower() == 'verde' or color.lower() == 'violeta':
    print(f'el color {color} es un color secundario')
else:
   print(f'el color {color} no es un color secundario')