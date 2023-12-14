import os
def menu():
    print("menu d opciones")
    print("1.- listar estaciones de ida")
    print("2.- listar estaciones de vuelta")
    print("3.- habilitar est intermedias")
    print("4.- venta de pasajes")
    print("5.- salir")
    opcion=int(input("ingrese una opcion: "))
    return opcion
def listarEstaciones(estaciones, tipo="ida"):
    print(f"Listado de estaciones de {tipo}")
    if tipo=="ida":
        for estacion in estaciones:
            if estacion["estado"]=="habilitado":
                print(f"id: {estacion['id']} nombre: {estacion['nombre']} hora de salida: {estacion['horaSalida']} estado: {estacion['estado']}")
    elif tipo == "vuelta":
        estaciones.reverse()
        for estacion in estaciones:
            if estacion["estado"]=="habilitado":
                print(f"id: {estacion['id']} nombre: {estacion['nombre']} hora de salida: {estacion['horaSalida']} estado: {estacion['estado']}")
        estaciones.reverse()
    else:
        print("tipo de viaje incorrecto ida/vuelta")
def listarTodasEstaciones(estaciones):
    print(f"Listado de estaciones")
    for estacion in estaciones:
        print(f"id: {estacion['id']} nombre: {estacion['nombre']} hora de salida: {estacion['horaSalida']} estado: {estacion['estado']}")
        
def habilitarEstacion(estaciones):
    print("habilitar estacion")
    listarTodasEstaciones(estaciones)
    id=int(input("ingrese el id de la estacion a habilitar:" ))
    for estacion in estaciones:
        if estacion["id"] == id:
            estacion["estado"]="habilitado"
            print("Estacion habilitada")
            return
    print(f"no se encontro la estacion con id {id}")
def venderPasaje(estaciones):
    print("Venta de pasajes")
    listarEstaciones(estaciones)
    estacionSalida=int(input("ingrese el id de salida: "))
    id = int(input("ingrese el id de la estacion de llegada: "))
    for estacion in estaciones:
        if estacion["id"]==id:
            if estacion["estado"]=="habilitado":
                print(f" id: {estacion['id']} estacion: {estacion['nombre']} hora ida {estacion['horaSalida']} ")
                print(f" id: {estacion['id']} estacion: {estacion['nombre']} hora regreso {estacion['horaLlegada']} ")
            else:
                resp=input("La estacion no esta hablilitada, la desea habilitar? s/n")
                if resp=="s":
                    estacion["estado"]="habilitado"
                    print("la estacion ya se encuenta habilitada para la venta de pasajes")
                    venderPasaje(estaciones)
            return
    print("no se encontro la estacion")


#programa principal
estaciones=[
    {"id":1,"nombre":"Paso de los Libres","horaSalida":"08:00","horaLlegada":"19:00","precioIda":0,"precioVuelta":1000,"estado":"habilitado"},
    {"id":2,"nombre":"Guaviraví","horaSalida":"08:45","horaLlegada":"18:15","precioIda":100,"precioVuelta":900,"estado":"Deshabilitado"},
    {"id":3,"nombre":"La Cruz","horaSalida":"09:30","horaLlegada":"17:30","precioIda":200,"precioVuelta":800,"estado":"habilitado"},
    {"id":4,"nombre":"Las Palmitas","horaSalida":"10:15","horaLlegada":"16:45","precioIda":300,"precioVuelta":700,"estado":"Deshabilitado"},
    {"id":5,"nombre":"Colonia Arrocera","horaSalida":"11:00","horaLlegada":"16:00","precioIda":400,"precioVuelta":600,"estado":"Deshabilitado"},
    {"id":6,"nombre":"Cuay Chico","horaSalida":"11:45","horaLlegada":"15:15","precioIda":500,"precioVuelta":500,"estado":"Deshabilitado"},
    {"id":7,"nombre":"Cuay Grande","horaSalida":"12:30","horaLlegada":"14:30","precioIda":600,"precioVuelta":400,"estado":"Deshabilitado"},
    {"id":8,"nombre":"Santo Tomé","horaSalida":"13:15","horaLlegada":"13:45","precioIda":700,"precioVuelta":300,"estado":"habilitado"},
    {"id":9,"nombre":"Tareirí","horaSalida":"14:00","horaLlegada":"13:00","precioIda":800,"precioVuelta":200,"estado":"Deshabilitado"},
    {"id":10,"nombre":"Virasoro","horaSalida":"14:45","horaLlegada":"12:15","precioIda":900,"precioVuelta":100,"estado":"habilitado"},
]
opcion=menu()
while opcion!= 5:
    if opcion== 1:
        listarEstaciones(estaciones)
    elif opcion==2:
        listarEstaciones(estaciones, "vuelta")
    elif opcion == 3 :
        habilitarEstacion(estaciones)
    elif opcion == 4:
        venderPasaje(estaciones)
    else:
        print("opcion incorrecta")
    opcion= menu()