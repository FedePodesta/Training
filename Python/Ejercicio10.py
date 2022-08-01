


# Ejercicio: El usuario debe adivinar un numero entre 0 y 10.
# el programa deberá pedir que el usuario introduzca un número 
# y debe decir si ha acertado, si el numero a adivinar es menor mayor que
# el que ha introducido

numeroadivinar = 7

while True:
    numerouser = int(input("Adivine el numero del 1 al 10: "))
    if numerouser < numeroadivinar:
        print(f"El numero secreto es mayor que { numerouser}")
        
    elif numerouser > numeroadivinar:
        print(f"El numero secreto es menor que { numerouser} ")
    else:
        if numeroadivinar == numerouser:
            print(f"HAS ACERTADO EL NUMERO ERA { numeroadivinar}")
            break

    
   
    


