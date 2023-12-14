def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError :
        print("error division por cero")
    else:
        print("el resultado es ",result)
    finally:
        print("adios !!")
divide(2,1)
divide(2,0)
divide(4,2)