class Mascotas:
    #defino los atributos
    mombre=str
    tipo=str
    dniDuenio=str
    anioNacimiento=int
    #defino el constructor
    def __init__(self, nom, tipo, dniDuenio, anioNac):
        self.nombre= nom
        self.tipo= tipo
        self.dniDuenio=dniDuenio
        self.anioNacimiento= anioNac
    #defino los metodos
    def calcularEdad(self, anioNac):
        fecha_actual = datetime.now()
        edad=fecha_actual.year-anioNac
        return edad
    def __str__(self):
        return (f"la mascota se llama {self.nombre}, es un {self.tipo}, y tiene: {self.calcularEdad(self.anioNacimiento)} años")