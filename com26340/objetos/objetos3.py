# defino la clase personas, para luego definir las clases alumnos y profesores
class personas:
    def __init__(self, nombre, apellido, dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
    #creo otro constructor solo con nombre y dni
    def __init__(self, nombre, dni):
        self.nombre=nombre
        self.dni=dni
        #creo otro constructor solo con nombre
    def __init__(self, nombre):
        self.nombre=nombre







    def __str__(self):
        return "nombre: " + self.nombre + " apellido: " + self.apellido + " dni: " + self.dni
    

# defino la clase alumno, que hereda de personas
class alumnos(personas):
    def __init__(self, nombre, apellido, dni, legajo, carrera):
        super().__init__(nombre, apellido, dni)
        self.legajo=legajo
        self.carrera=carrera
    def __str__(self):
        return super().__str__() + " legajo: " + self.legajo + " carrera: " + self.carrera
    

# defino la clase profesor, que hereda de personas
class profesores(personas):
    def __init__(self, nombre, apellido, dni, legajo, cargo):
        super().__init__(nombre, apellido, dni)
        self.legajo=legajo
        self.cargo=cargo
    def __str__(self):
        return super().__str__() + " legajo: " + self.legajo + " cargo: " + self.cargo
    
    
#creo un alumno y un profesor
alumno1=alumnos("juan","perez","45639963","1234","programacion")
profesor1=profesores("carlos","gonzalez","54675576","1234","titular")
#imprimo los datos de alumno y profesor
print(alumno1)
print(profesor1)


