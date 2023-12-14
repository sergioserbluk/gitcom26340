alumnos={
    23050:{"Apellido": "Rios", "Nombre":"juan","nota1":8},
    23051:{"Apellido": "Rojas", "Nombre":"Ana","nota1":9},
    23052:{"Apellido": "Sosa", "Nombre":"Ester","nota1":7}
}

for clave, valor in alumnos.items():
    print(f"El alumno con el legajo N° {clave} se llama {alumnos[clave]['Nombre']} {alumnos[clave]['Apellido']} y su nota fue {alumnos[clave]['nota1']}")