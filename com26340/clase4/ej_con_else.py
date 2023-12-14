cadena="hola"
le=input("ingrese una letra a buscar: ")
for letra in cadena:
    if letra==le:
        print("encontrada")
        break
else:
    print("la letra no se encuentra en la secuencia")