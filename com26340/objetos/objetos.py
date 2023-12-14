from datetime import datetime
class mascotas:
    #defino los atributos (definidos como publicos)
    nombre=str
    tipo=str
    dni_propietario=int
    sonido=str
    __anio_nac=int
    #creo el metodo constructor
    def __init__(self,nombre, tipo, dni_propietario, sonido,anio_nac):
        self.nombre=nombre
        self.tipo=tipo
        self.dni_propietario=dni_propietario
        self.sonido=sonido
        self.__anio_nac=anio_nac
    #defino los metodos de clase
    def comunicarse(self):
        print(f"{self.nombre} esta {self.sonido}")
    def obtener_edad(self):
        anio=datetime.now().year
        print(type(anio))
        print(f"la mascota tiene {int(anio) - int(self.__anio_nac) } años")
    def __str__(self):
        return "nombre: " + self.nombre + " año nac: " + str(self.__anio_nac)
    
#creo mascotas        
mimascota=mascotas("coca","perro", "45639963", "ladrando",2010)
mascotadeJuan=mascotas("felpita","gato","54675576","maullando",2015)
mimascota.comunicarse()
mascotadeJuan.comunicarse()
print(f"el dni del dueño de {mimascota.nombre} es {mimascota.dni_propietario}")
print(mimascota)
print(mascotadeJuan)
anio=anio=datetime.now().year
mimascota.obtener_edad()
print(mimascota)
print(mascotadeJuan)