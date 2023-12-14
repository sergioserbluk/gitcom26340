from openpyxl import Workbook
# crear el objeto workbook
wb=Workbook()
# nombre del archivo
archivo="datos.xlsx"
hoja1=wb.active
hoja1.title="inicial"

hoja1["A1"]="hola"
hoja1["B1"]="clase"
#guardo el archivo
wb.save(filename=archivo)
print(hoja1["B1"].value)