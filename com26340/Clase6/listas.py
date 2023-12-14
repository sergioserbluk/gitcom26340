milista=[1,2,3]
milista.append(5)
print(milista)
milista.insert(3,4)
otralista=[6,7,8]
milista.extend(otralista)
for elemento in milista:
    print(elemento)