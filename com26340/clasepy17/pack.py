from tkinter import *
from tkinter import messagebox
#creo una ventana de login usando Tkinter y pack
ventana = Tk()
ventana.title("Login")
ventana.geometry("300x300")
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
usuario_label.pack(anchor=NW,padx=10,pady=10)
#creo un entry para el usuario y lo empaqueto al lado del label
usuario = StringVar()
usuario_entry = Entry(ventana, textvariable=usuario)
usuario_entry.pack(anchor=NW,padx=10,pady=10)

#creo un label para la contraseña
password_label = Label(ventana, text="Contraseña: ",bg="brown",fg="white")
password_label.pack(anchor=NW,padx=10,pady=10)

#creo un entry para la contraseña
password = StringVar()
password_entry = Entry(ventana, textvariable=password,show="*")
password_entry.pack(anchor=W,padx=10,pady=10)
#creo un boton para validar
validar_button = Button(ventana, text="Validar", command=validar)
validar_button.pack(anchor=NW,padx=10,pady=10)
#ejecuto la ventana
ventana.mainloop()
