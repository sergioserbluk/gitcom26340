from tkinter import *
from tkinter import messagebox
#creo una ventana de login usando Tkinter y grid
ventana = Tk()
ventana.title("Login")
ventana.geometry("250x150")
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
usuario_label = Label(ventana, text="Usuario: ",bg="brown",fg="white", justify=LEFT)
usuario_label.grid(row=0,column=0,padx=10,pady=10, sticky="E")
#creo un label para la contraseña
password_label = Label(ventana, text="Contraseña: ",bg="brown",fg="white", justify=LEFT)
password_label.grid(row=1,column=0,padx=10,pady=10)
#creo un entry para el usuario
usuario = StringVar()
usuario_entry = Entry(ventana, textvariable=usuario,border=2)
usuario_entry.grid(row=0,column=1,padx=10,pady=10)
#creo un entry para la contraseña
password = StringVar()
password_entry = Entry(ventana, textvariable=password,show="*", border=2)
password_entry.grid(row=1,column=1,padx=10,pady=10)
#creo un boton para validar
validar_button = Button(ventana, text="Validar", command=validar)
validar_button.grid(row=2,column=0,padx=10,pady=10, columnspan=2)
#ejecuto la ventana
ventana.mainloop()
