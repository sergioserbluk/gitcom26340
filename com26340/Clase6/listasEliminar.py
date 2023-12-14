'''
lista=[1,2,3,4,5,6]
print(f"lista original {lista}")
lista.pop(3)
print(f"lista luego del pop {lista}")
'''
'''
lista=[1,2,3,4,5,6]
print(f"lista original {lista}")
lista.remove(3)
print(f"lista luego del remove {lista}")
lista.clear()
print(lista)
'''
'''
lista=[1,2,3,4,5,6, 4]
print(f"lista original {lista}")
ie=lista.index(4)
print(ie)
lista[0]=7
print(lista)
valor=lista[2]
print(valor)
'''
lista=[1,2,3,4,5,6, 4]
print(f"lista original {lista}")
listanueva=lista[2:5]
print(f"lista original {lista}")
print(f"lista nueva {listanueva}")
del(lista[0])
print(lista)