import os
while True:
    os.system('cls')
    print("1 para continuar")
    print("2 para salir")
    op=int(input("ingrese una opcion "))
    if op ==2:
        break
    print("************lista de estaciones*****************")
    list_paradas=[[1, 'Paso de los Libres', True] ,[2, 'Guaviravi',False],[3,'La Cruz',True],[4 ,'Las Palmitas',False],[5, 'Col Arrocera',False],[6, 'Cuay Chico', False],[7, 'Cuay Grande', False], [8,'Santo Tome', True], [9 ,'Tareiri',False],[10,'Gobernador Virasoro',True]]
    for paradas in list_paradas:
        if paradas[2]==True:
            print(f"{paradas[0]} - {paradas[1]}")

    #habilito guaviravi
    list_paradas[1][2]=True
    for paradas in list_paradas:
        if paradas[2]==True:
            print(f"{paradas[0]} - {paradas[1]}")

    # muestro las intermedias en False
    print("*********intermedias a habilitar**********")
    for paradas in list_paradas:
        if paradas[2]==False:
            print(f"{paradas[0]} - {paradas[1]}")
    ie=int(input("ingrese el numero de estacion a habilitar: "))
    list_paradas[ie-1][2]=True
    print("**************estaciones habilitadas**************")
    for paradas in list_paradas:
        if paradas[2]==True:
            print(f"{paradas[0]} - {paradas[1]}")
    input("presione una tecla para continuar...")