import datetime

class Persona:
    #defino los atributos
    __nombre=str
    __anioNac=int
    __edad=int
    
    def __init__(self, nombre, anionacimiento):
        self.__nombre = nombre
        self.__anioNac = anionacimiento
    

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        year=datetime.datetime.now().year
        self.__edad=year- self.__anioNac
        return self.__edad 

# Crear una instancia de la clase Persona
persona = Persona("Juan", 1980)

# Acceder a los atributos mediante los métodos get
print(persona.get_nombre())  # Imprime: Juan
print(persona.get_edad())    # Imprime: 
persona.set_nombre("Juan Manuel")
print(persona.get_nombre())
otrapersona=Persona("laura")
print(otrapersona.get_nombre())
## Intentar acceder directamente a los atributos privados genera un error
##print(persona.__nombre)  # Genera un error
#
## Cambiar los atributos mediante los métodos set
#persona.set_nombre("Juan Carlos")
#
#
#print(persona.get_nombre())  # Imprime: Carlos
#print(persona.get_edad())    # Imprime: 

