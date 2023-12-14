def mayoriaedad(ed):
    if ed >= 18:
        return "si puede pasar"
    return "no puede pasar"
edad=int(input("ingrese su edad en años: "))
print(mayoriaedad(edad))
    