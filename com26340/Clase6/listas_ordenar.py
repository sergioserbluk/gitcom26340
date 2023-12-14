'''
list_num=[3,5.1,7,8.3,6,4,3,7,3]
list_frutas=["manzana", "anana", "banana", "kiwi"]
print(f"lista original {list_num}")
print(f"lista original {list_frutas}")
list_num.sort()
list_frutas.sort()
print(f"lista luego del sort {list_num}")
print(f"lista luego del sort {list_frutas}")
list_frutas.sort(reverse=True)
list_num.sort(reverse=True)
print(f"lista luego del sort de mayor a menor {list_num}")
print(f"lista luego del sort de mayor a menor {list_frutas}")
print(f"la lista de frutas tiene {len(list_frutas)} elementos")
print(f"la lista de números tiene {len(list_num)} elementos")
'''

list_num=[3,5.1,7,8.3,6,4,3,7,3]
cant_el=len(list_num)
el_a_b=int(input("ingrese el número que quiere saber si se encuentra: "))
print(f" el número {el_a_b} se ecuentra {list_num.count(el_a_b)} veces")
