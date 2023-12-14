from tkinter import *
def ejecutar(f):
    v0.after(200,f)
def mostrar(ventana):
    ventana.deiconify()
def ocultar(ventana):
    ventana.withdraw()
v0=Tk()
v0.config(bg="black")
v0.geometry("400x400")
b1=Button(v0,text="abrir v1", command=lambda:ejecutar(mostrar(v1)))
b1.grid(row=1, column=1)
b2=Button(v0,text="cerrar v1", command=lambda:ejecutar(ocultar(v1)))
b2.grid(row=1,column=2)
v1=Toplevel(v0)
v1.withdraw()

v0.mainloop()