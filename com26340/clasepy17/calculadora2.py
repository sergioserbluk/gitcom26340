from tkinter import *
import math
                                  ## CREO LAS VENTANAS ##
ventana1=Tk()
ventana1.config(bg="white")
ventana1.geometry("330x440")
ventana1.title("🖩Calculadora Basica by Ale🖩")
ventana2=Toplevel(ventana1)
ventana2.config(bg="white")
ventana2.title("🖩Calculadora Cientific. by Ale🖩")
ventana2.geometry("459x455")
i=0
         ##### A CONTINUACION, CREO UN FRAME PARA LAS DOS VENTANAS PARA DARLE UN FORMATO A LA CALCULADORA###
frame1=Frame(ventana1, padx=10, pady=10, bd=2, bg="gray", relief="groove")
frame1.grid(padx=10, pady=10)
frame2=Frame(ventana2, padx=10, pady=10, bd=2, bg="gray", relief="groove")
frame2.grid(padx=10, pady=10)
         ##CREO DISPLAY DE LA CALC.BASICA, EL CUAL HABRA UNO PARA EL CALCULO Y OTRO PARA EL RESULTADO###
displaynm1calc=Entry(frame1,font=('arial',18, 'bold'), bd=10, width= 15, bg="cadetblue", justify=RIGHT)
displaynm1calc.grid(row=1, column=0 , columnspan=3, sticky=W+E+S+N, pady=1) 
displaynm1res=Entry(frame1,font=('arial',16, 'bold'), bd=6, width= 6, bg="black", fg="white", justify=RIGHT)
displaynm1res.grid(row=0, column=0 , columnspan=3, pady=1) 
         ##CREO DISPLAY DE LA CALC.CIENTIFICA, EL CUAL HABRA UNO PARA EL CALCULO Y OTRO PARA EL RESULTADO###
displaynm2calc=Entry(frame2,font=('arial',18, 'bold'), bd=10, width= 15, bg="cadetblue", justify=RIGHT)
displaynm2calc.grid(row=1, column=1 , columnspan=4, sticky=W+E+S+N, pady=1) 
displaynm2res=Entry(frame2,font=('arial',18, 'bold'), bd=10, width= 15, bg="black", fg="white", justify=RIGHT)
displaynm2res.grid(row=0, column=1 , columnspan=4 ,sticky=W+E+S+N,pady=1)
                                        
                                        ##DEFINO FUNCIONES
def click_boton (valor):  ##FUNCION QUE ME PERMITE MOSTRAR EL VALOR DEL BOTON ACCIONADO EN DISPLAY
    global i
    displaynm1calc.insert(i, valor)
    displaynm2calc.insert(i, valor)
    i+=1
    
def operaciones():        ##FUNCION QUE ME PERMITE REALIZAR OPERACIONES AL MOMENTO DE TOCAR EL =
    ecuacion=displaynm1calc.get()
    ecuacion=displaynm2calc.get()
    try:   
        resultado=eval(ecuacion)
        displaynm1res.delete(0,END)
        displaynm1res.insert(0, resultado)
        displaynm2res.delete(0,END)
        displaynm2res.insert(0, resultado)
        displaynm1calc.delete(0,END)
        displaynm2calc.delete(0,END)
    except:
        displaynm1res.delete(0, END)
        displaynm1res.insert(0, "ERROR")
        displaynm2res.delete(0,END)
        displaynm2res.insert(0, "ERROR")
def sin_funcion():     ###FUNCION TRIGONOMETRICA SENO###
        valor=float(displaynm2calc.get())
        resultado=math.sin(math.radians(valor))
        displaynm2res.delete(0, END)
        displaynm2res.insert(0, resultado)
        displaynm2calc.delete(0, END)
def cos_funcion():      ###FUNCION TRIGONOMETRICA COSENO###
        valor=float(displaynm2calc.get())
        resultado=math.cos(math.radians(valor))
        displaynm2res.delete(0, END)
        displaynm2res.insert(0, resultado)
        displaynm2calc.delete(0, END)
def tan_funcion():      ###FUNCION TRIGONOMETRICA TANGENTE###
        valor=float(displaynm2calc.get())
        resultado=math.tan(math.radians(valor))
        displaynm2res.delete(0, END)
        displaynm2res.insert(0, resultado)
        displaynm2calc.delete(0, END)
def log_funcion():     ###FUNCION LOGARITMO###
    valor=float(displaynm2calc.get())
    resultado=math.log10(valor)
    displaynm2res.delete(0, END)
    displaynm2res.insert(0, resultado)
    displaynm2calc.delete(0, END)
def cuadrado_funcion():  ###FUNCION VALOR AL CUADRADO###
     valor=float(displaynm2calc.get())
     resultado=valor**2
     displaynm2res.delete(0, END)
     displaynm2res.insert(0, resultado)
     displaynm2calc.delete(0, END)
def cubo_funcion():       ###FUNCION POTENCIA ELEVADA A EXPONENTE DESEADO (FALTA DESARROLLAR)###
     valor=float(displaynm2calc.get())
     resultado=valor**3
     displaynm2res.delete(0, END)
     displaynm2res.insert(0, resultado)
     displaynm2calc.delete(0, END)
def porcentaje_funcion(): ###FUNCION % DE UN VALOR (FALTA DESARROLLAR)###
     valor=float(displaynm2calc.get())
     resultado=valor/100
     displaynm2res.delete(0, END)
     displaynm2res.insert(0, resultado)
     displaynm2calc.delete(0, END)
def raiz_funcion():      ###FUNCION PARA CALCULAR RAIZ DE UN NUMERO###
     valor=float(displaynm2calc.get())
     resultado=math.sqrt(valor)
     displaynm2res.delete(0, END)
     displaynm2res.insert(0, resultado)
     displaynm2calc.delete(0, END)
def pi_funcion():       ###FUNCION VALOR PI###
        valor=float(displaynm2calc.get())
        resultado=math.pi*valor
        displaynm2res.delete(0, END)
        displaynm2res.insert(0, resultado)
        displaynm2calc.delete(0, END)
def factorial_funcion():
    valor = int(displaynm2calc.get())
    resultado = math.factorial(valor)
    displaynm2res.delete(0, END)
    displaynm2res.insert(0, resultado)
    displaynm2calc.delete(0, END)
def borrar():          ##FUNCION QUE PERMITE BORRAR TODO EL CONTENIDO DEL DISPLAY##
    displaynm1res.delete(0,END)
    displaynm2res.delete(0, END)
    displaynm1calc.delete(0,END)
    displaynm2calc.delete(0, END)
def borrarcarac():
     displaynm1calc.delete(len(displaynm1calc.get())-1, END)
     displaynm2calc.delete(len(displaynm2calc.get())-1, END)

def mostrar(ventana):ventana.deiconify()   ##MOSTRAR VENTANA
def ocultar(ventana):ventana.withdraw()    ##OCULTAR PANTALLA
def ejecutar(f):ventana1.after(200,f)      ##EJECUTAR FUNCION
                ##EN UNA FUNCION DEFINO TODOS LOS BOTONES DE MI CALCULADORA CIENTIFICA##
def calcient():           
    num1=Button(frame2, text="1", width=8, height=3, bg="sky blue", pady=3, padx=3, command=lambda: click_boton(1)).grid(row=5,column=0)
    num2=Button(frame2, text="2", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(2)).grid(row=5,column=1)
    num3=Button(frame2, text="3", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(3)).grid(row=5,column=2) 
    num4=Button(frame2, text="4", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(4)).grid(row=4,column=0)
    num5=Button(frame2, text="5", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(5)).grid(row=4,column=1)
    num6=Button(frame2, text="6", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(6)).grid(row=4,column=2)
    num7=Button(frame2, text="7", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(7)).grid(row=3,column=0)
    num8=Button(frame2, text="8" , width=8, height=3, bg="sky blue",pady=3, padx=3, command=lambda: click_boton(8)).grid(row=3,column=1)
    num9=Button(frame2, text="9", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(9)).grid(row=3,column=2)
    num0=Button(frame2, text="0", width=8, height=3, bg="sky blue", pady=3, padx=3,command=lambda: click_boton(0)).grid(row=6,column=0)
    botonborrartd=Button(frame2,text="AC", fg="red", width=8, height=3,pady=3, padx=3,command=lambda: borrar()).grid(row=2, column=0)
    botonborrarcarac=Button(frame2, text="←", fg="yellow", bg="#461683",width=5, height=2, pady=1, padx=1, command=lambda: borrarcarac()).grid(row=1, column=5)
    parentesis1=Button(frame2, text="(", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("(")).grid(row=2,column=1)
    parentesis2=Button(frame2, text=")", width=8, height=3,pady=3, padx=3,command=lambda: click_boton(")")).grid(row=2,column=2)
    botonpunto=Button(frame2, text=".", width=8, height=3,pady=3, padx=3,command=lambda: click_boton(".")).grid(row=6, column=1)
    botondividir=Button(frame2, text="/", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("/")).grid(row=2, column=3)
    botonmult=Button(frame2, text="*", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("*")).grid(row=3, column=3)
    botonsuma=Button(frame2, text="+", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("+")).grid(row=4, column=3)
    botonresta=Button(frame2, text="-", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("-")).grid(row=5, column=3)
    botonigual=Button(frame2, text="=", bg="#272724", fg="white",width=8, height=3,pady=3, padx=3,command=lambda: operaciones()).grid(row=6,column=2, columnspan=2, sticky=W+E)
    botoncos=Button(frame2, text="cos", bg="#E3DE79", width=8, height=3,pady=3, padx=3,command=lambda: cos_funcion() ).grid(row=2, column=4)
    botonrtan=Button(frame2, text="tan", width=8,bg="#E3DE79", height=3,pady=3, padx=3,command=lambda: tan_funcion()).grid(row=2, column=5)
    botonsin=Button(frame2, text="sin", width=8,bg="#E3DE79", height=3,pady=3, padx=3,command=lambda: sin_funcion()).grid(row=3, column=4)
    botonrlog=Button(frame2, text="log", width=8,bg="#E3DE79", height=3,pady=3, padx=3,command=lambda: log_funcion()).grid(row=3, column=5)
    botonrporc=Button(frame2, text="%", width=8,bg="#E3DE79", height=3,pady=3, padx=3,command=lambda: porcentaje_funcion()).grid(row=4, column=4)
    botonrpi=Button(frame2, text="π", width=8,bg="#E3DE79", height=3,pady=3, padx=3,command=lambda: pi_funcion()).grid(row=4, column=5) 
    botonrcuadrado=Button(frame2, text="x²",bg="#E3DE79", width=8,pady=3, padx=3, height=3,command=lambda: cuadrado_funcion()).grid(row=5, column=4)
    botonrcubo=Button(frame2, text="x3",bg="#E3DE79", width=8,pady=3, padx=3, height=3,command=lambda:cubo_funcion()).grid(row=5, column=5)
    botonrraiz=Button(frame2, text="√",bg="#E3DE79", width=8, height=3,pady=3, padx=3,command=lambda: raiz_funcion()).grid(row=6, column=4)
    botonfact=Button(frame2, text="n!",bg="#E3DE79", width=8, height=3,pady=3, padx=3,command=lambda:factorial_funcion() ).grid(row=6, column=5)
    botoncalcbas=Button(frame2, text="C.BAS", width=5, height=2,bg="black", fg="white", command=lambda: ejecutar(mostrar(ventana1),ocultar(ventana2))).grid(row=0, column=5,padx=5, pady=5, sticky=E+W )

                            ##AQUI DESARROLLO MI CALCULADORA CON FUNCIONES BASICAS##
ejecutar(ocultar(ventana2))
num1=Button(frame1, text="1", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(1)).grid(row=5,column=0)
num2=Button(frame1, text="2", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(2)).grid(row=5,column=1)
num3=Button(frame1, text="3", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(3)).grid(row=5,column=2) 
num4=Button(frame1, text="4", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(4)).grid(row=4,column=0)
num5=Button(frame1, text="5", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(5)).grid(row=4,column=1)
num6=Button(frame1, text="6", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(6)).grid(row=4,column=2)
num7=Button(frame1, text="7", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(7)).grid(row=3,column=0)
num8=Button(frame1, text="8" , width=8, height=3, pady=3, padx=3,bg="sky blue",command=lambda: click_boton(8)).grid(row=3,column=1)
num9=Button(frame1, text="9", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(9)).grid(row=3,column=2)
num0=Button(frame1, text="0", width=8, height=3,pady=3, padx=3, bg="sky blue",command=lambda: click_boton(0)).grid(row=6,column=0)
botonborrartd=Button(frame1,text="AC", fg="red", width=8, height=3,pady=3, padx=3,command=lambda: borrar()).grid(row=2, column=0)
botonborrarcarac=Button(frame1, text="←", fg="yellow", bg="#461683",width=5, height=2, pady=1, padx=1, command=lambda: borrarcarac()).grid(row=1, column=3)
parentesis1=Button(frame1, text="(", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("(")).grid(row=2,column=1)
parentesis2=Button(frame1, text=")", width=8, height=3,pady=3, padx=3,command=lambda: click_boton(")")).grid(row=2,column=2)
botonpunto=Button(frame1, text=".", width=8, height=3,pady=3, padx=3,command=lambda: click_boton(".")).grid(row=6, column=1)
botondividir=Button(frame1, text="/", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("/")).grid(row=2, column=3)
botonmult=Button(frame1, text="x", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("*")).grid(row=3, column=3)
botonsuma=Button(frame1, text="+", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("+")).grid(row=4, column=3)
botonresta=Button(frame1, text="-", width=8, height=3,pady=3, padx=3,command=lambda: click_boton("-")).grid(row=5, column=3)
botonigual=Button(frame1, text="=",  bg="#272724", fg="white", width=8, height=3,pady=3, padx=3,command=lambda: operaciones()).grid(row=6,column=2, columnspan=3, sticky=W+E)
                                ##BOTON PARA ENTRAR A CALCULADORA CIENTIFICA
botoncientif=Button(frame1, text="Calc.Cient", width=5, height=2 , bg="black", fg="white",command=lambda:ejecutar (ocultar(ventana1),mostrar(ventana2))).grid(row=0, column=3, sticky=W+E)
calcient() ##llamo a calculadora cientifica


ventana1.mainloop()
ventana2.mainloop()

