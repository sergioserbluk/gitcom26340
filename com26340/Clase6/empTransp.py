list_estaciones=["Paso De Los Libres", "La Cruz", "Santo Tomé", "Gobernador Virasoro"]
while True:
    print("1 para ida")
    print("2 para regreso")
    op=input("seleccione el viaje")
    if op=="1":
        print("********Lista de estaciones de ida **********")
        for est in list_estaciones:
            print(est)
    if op =="2":
        print("********Lista de estaciones de regreso **********")
        list_estaciones.reverse()
        for est in list_estaciones:
            print(est)
        list_estaciones.reverse()
    else:
        print("adios!")
        break
