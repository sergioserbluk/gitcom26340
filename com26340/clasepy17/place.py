from tkinter import *
from tkinter import messagebox
#creo una ventana de login usando Tkinter
ventana = Tk()
ventana.title("Login")
ventana.geometry("300x150+1200+300")
ventana.resizable(False,False)



ventana.config(bg="brown")
#creo una funcion para validar el usuario y contraseña
def validar():
    if usuario.get() == "admin" and password.get() == "123":
        #muestro un cuadro de dialogo
        messagebox.showinfo("Login","Usuario y contraseña correctos")
    else:
        #muestro un cuadro de dialogo
        messagebox.showerror("Login","Usuario y contraseña incorrectos")
#creo un label para el usuario
usuario_label = Label(ventana, text="Usuario: ",bg="brown",fg="white")
usuario_label.place(x=10,y=10)
#creo un label para la contraseña
password_label = Label(ventana, text="Contraseña: ",bg="brown",fg="white")
password_label.place(x=10,y=40)
#creo un entry para el usuario
usuario = StringVar()
usuario_entry = Entry(ventana, textvariable=usuario)
usuario_entry.place(x=100,y=10)
#creo un entry para la contraseña
password = StringVar()
password_entry = Entry(ventana, textvariable=password,show="*")
password_entry.place(x=100,y=40)
#creo un boton para validar
validar_button = Button(ventana, text="Validar", command=validar,width=20)
validar_button.place(x=80,y=90)
#ejecuto la ventana
ventana.mainloop()

