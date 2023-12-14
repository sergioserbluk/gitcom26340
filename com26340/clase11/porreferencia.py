#funcion que retorna el doble de los elementos de una coleccion 
def doblarnro(nros):
    for indice in range(len(nros)):
        nros[indice]=nros[indice] * 2
    return nros
# aca inicia el programa
minros = [10, 20, 5]
print(doblarnro(minros))
print(minros)